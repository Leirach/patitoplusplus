import semanticTable as semantics
import functionDirectory as fm
import exceptions

class CodeGenerator:
    def __init__(self, filename="patito"):
        self.f = open(filename+".obj", "w")
        self.code = ["Goto main"]
        self.line = 2
        # expresions
        self.opStack = []
        self.idStack = []
        self.tpStack = []
        # functions and variables
        self.funcDir = fm.FunctionManager()
        self.gotoStack = []
        self.pendingLines = []
        self.paramCounter = 0
        self.forIds = []
        self.temp = 1
        # Memory
        self.memStack = []

    def __del__(self):
        mem = self.funcDir.createConstTable()
        for line in self.code:
            self.f.write(line)
        self.f.write("\n")
        for line in mem:
            self.f.write(line)
        self.f.close()

    # -- Utilities --
    def writeQuad(self, tok1, tok2, tok3, tok4):
        buf = "%s %s %s %s\n" % (tok1, tok2, tok3, tok4)
        self.code.append(buf)
        self.line += 1

    def popVar(self):
        var = self.idStack.pop()
        tipo = self.tpStack.pop()
        mem = self.memStack.pop()
        return var, tipo, mem

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]    # this will get the last element of stack
        else:
            return None

    # -- BUILD EXPRESSIONS AND ASSIGMENT --
    def buildExp(self):
        op = self.opStack.pop()
        # pop ids from stack
        der, derType, derMemScope = self.popVar()
        izq, izqType, izqMemScope = self.popVar()
        # get next temp var
        aux = "t"+str(self.temp)
        auxType = semantics.match(op, izqType, derType)
        if auxType is None:
            exceptions.fatalError("Invalid operand %s for types %s and %s" % (op, izqType, derType))
        izqAddr = self.funcDir.getAddress(izq, izqMemScope, izqType)
        derAddr = self.funcDir.getAddress(der, derMemScope, derType)
        auxAddr = self.funcDir.getAddress(aux, 'temp', auxType)
        self.writeQuad(op, izqAddr, derAddr, auxAddr)
        self.idStack.append(aux)
        self.tpStack.append(auxType)
        self.memStack.append('temp')
        self.temp += 1

    # TODO incompleto
    def buildUnaryExp(self):
        op = self.opStack.pop()
        # 
        if op == '-': # no estoy seguro si esto funciona
            self.opStack.append('*')
            self.idStack.append('-1')
            self.tpStack.append('int')
            self.memStack.append('const')
            self.buildExp()
        # falta para '$', '^', '!'

    def buildAssign(self):
        op = '='
        val, valType, valMem = self.popVar()
        var, varType, varMem = self.popVar()
        matches = semantics.match(op, varType, valType)
        if matches is None:
            exceptions.fatalError("No se puede asignar tipo %s a variable de tipo %s" % (valType, varType))
        valAddr = self.funcDir.getAddress(val, valMem, valType)
        varAddr = self.funcDir.getAddress(var, varMem, varType)
        self.writeQuad('=', valAddr, '0', varAddr)

    # -- IF ELSE / SI ENTONCES SINO--
    def ifStart(self):
        cond, condType, condMemScope = self.popVar()
        if condType not in ['bool']:
            exceptions.fatalError("Se esperaba bool en condicional se leyó %s" % (condType))
        condAddr = self.funcDir.getAddress(cond, condMemScope, condType)
        buf = "gotof %s" %(condAddr)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.writeQuad('if', 'gotof', 'temp', '0') # temporal quadruple

    def ifElse(self):
        self.writeQuad('else', 'goto', 'temp', '0')
        self.ifEnd()
        buf = "goto"
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line-1)

    def ifEnd(self):
        target = self.line
        lineNo = self.gotoStack.pop()
        buf = "%s %d 0 0\n" % (self.pendingLines.pop(), target)
        self.code[lineNo-1] = buf

    # -- WHILE / MIENTRAS HAZ --
    def whileStart(self):
        self.gotoStack.append(self.line)

    def whileDo(self):
        cond, condType, condMemScope = self.popVar() # TODO Checar que sea bool (int tambien?)
        if condType not in ['bool']:
            exceptions.fatalError("Se esperaba bool en ciclo mientras, se recibió %s" % (condType))
        condAddr = self.funcDir.getAddress(cond, condMemScope, condType)
        buf = "gotof %s" % (condAddr)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.writeQuad('while', 'goto', 'temp', '0')

    def whileEnd(self):
        lineNo = self.gotoStack.pop()
        buf = "%s %d 0\n" % (self.pendingLines.pop(), self.line+1)
        self.code[lineNo-1] = buf
        retLine = self.gotoStack.pop()
        self.writeQuad('goto', retLine, '0', '0')

    # -- FOR / DESDE HASTA HACER --
    def forStart(self):
        val, valType, valMem = self.popVar()
        inc, incType, incMem = self.popVar()
        if  valType not in ['int', 'float']:
            exceptions.fatalError("Se esperaba variable int o float para iterar en 'desde', se recibió %s" %(valType))
        valAddr = self.funcDir.getAddress(val, valMem, valType)
        incAddr = self.funcDir.getAddress(inc, incMem, incType)
        self.writeQuad("=", valAddr, "0", incAddr)
        self.idStack.append(inc)
        self.tpStack.append(incType)
        self.memStack.append(incMem)
        self.forIds.append(incAddr)
        self.gotoStack.append(self.line)

    def forDo(self):
        self.opStack.append("<=")
        self.buildExp()
        cond, condType, condMemScope = self.popVar()
        condAddr = self.funcDir.getAddress(cond, condMemScope, condType)
        self.gotoStack.append(self.line)
        buf = "gotof %s" % (condAddr)
        self.pendingLines.append(buf)
        self.writeQuad('loop', 'gotof', 'temp', '0')

    def forEnd(self):
        incAddr = self.forIds.pop()
        # la maquina virtual puede hacer incrementos aunque en teoria se deberia 
        # usar un temporal para esta suma
        self.writeQuad('+', incAddr, 1, incAddr)
        pendingIdx = self.gotoStack.pop() - 1
        retLine = self.gotoStack.pop()
        self.writeQuad('goto', str(retLine), '0', '0')
        buf = "%s %d 0 0\n" % (self.pendingLines.pop(), self.line)
        self.code[pendingIdx] = buf


    # -- FUNCDIR Y VARIABLES --
    def registerVariable(self, var, varType):
        self.funcDir.registerVariable(var, varType)

    def getVarType(self, p):
        return self.funcDir.getVariableType(None, p) #default scope

    def registerFunc(self, functionName, functionType):
        if functionName == 'principal':
            self.code[0] = "goto %d 0 0\n" %(self.line)
        self.funcDir.registerFunc(functionName, functionType)

    def registerFuncParams(self, paramId, paramType):
        self.funcDir.registerFuncParams(paramId, paramType) 

    def endFunc(self):
        # calcular tamaño de todo, self.temp tiene el count
        self.temp = 1 # reset temp counter
        self.code.append("ENDFUNC\n")
        self.line += 1
        self.funcDir.endFunc()

    # -- LLAMADAS DE FUNCIONES --
    def funcCallStart(self, func_id):
        #check if functions exists in directory?
        self.funcDir.callFunction(func_id)
        self.idStack.append(func_id)
        self.writeQuad('ERA', func_id, '0', '0')

    def funcCallParam(self):
        param, paramType, paramMemScope = self.popVar()
        calledFunc = self.peek(self.idStack)
        self.funcDir.validateParam(calledFunc, self.paramCounter, paramType)
        self.paramCounter += 1 # param counting starts at 0
        paramAddr = self.funcDir.getAddress(param, paramMemScope, paramType)
        aux = 'par'+str(self.paramCounter)
        self.writeQuad('PARAM', paramAddr, aux, '0')

    def funcCallEnd(self):
        func_id = self.idStack.pop()
        self.writeQuad('GOSUB', func_id, '0', '0')
        self.paramCounter = 0 # reset param counter
        # funcDir.validateFunctionSemantics(func_id)

    # -- READ PRINT / QUACKIN QUACKOUT --
    def ioQuad(self, io):
        var, varType, varMemScope = self.popVar()
        varAddr = self.funcDir.getAddress(var, varMemScope, varType)
        self.writeQuad(io, varAddr, '0','0')

