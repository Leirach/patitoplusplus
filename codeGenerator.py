import semanticTable as semantics
import functionDirectory as fm
import exceptions

class CodeGenerator:
    def __init__(self, filename="patito"):
        self.f = open(filename+".obj", "w")
        self.code = ["gosub principal\n"]
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
        izqAddr = self.funcDir.getAddress(izq, izqType, izqMemScope)
        derAddr = self.funcDir.getAddress(der, derType, derMemScope)
        auxAddr = self.funcDir.getAddress(aux, auxType, 'temp')
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
        valAddr = self.funcDir.getAddress(val, valType, valMem)
        varAddr = self.funcDir.getAddress(var, varType, varMem)
        self.writeQuad('=', valAddr, '0', varAddr)

    # -- IF ELSE / SI ENTONCES SINO--
    def ifStart(self):
        cond, condType, condMemScope = self.popVar()
        if condType not in ['bool']:
            exceptions.fatalError("Se esperaba bool en condicional se leyó %s" % (condType))
        condAddr = self.funcDir.getAddress(cond, condType, condMemScope)
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
        condAddr = self.funcDir.getAddress(cond, condType, condMemScope)
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
        valAddr = self.funcDir.getAddress(val, valType, valMem)
        incAddr = self.funcDir.getAddress(inc, incType, incMem)
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
        condAddr = self.funcDir.getAddress(cond, condType, condMemScope)
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
    def registerVariable(self, var, varType, dim1=None, dim2=None):
        self.funcDir.registerVariable(var, varType, dim1, dim2)

    def getVarType(self, p):
        return self.funcDir.getVariable(p)['type']

    def registerFunc(self, functionName, functionType):
        self.funcDir.registerFunc(functionName, functionType, self.line)

    def registerFuncParams(self, paramId, paramType):
        self.funcDir.registerFuncParams(paramId, paramType)

    def endFunc(self):
        # calcular tamaño de todo, self.temp tiene el count
        self.temp = 1 # reset temp counter
        self.code.append("ENDFUNC 0 0 0\n")
        self.line += 1
        self.funcDir.endFunc(self.temp)

    # -- LLAMADAS DE FUNCIONES --
    def funcCallStart(self, func_id):
        self.funcDir.callFunction(func_id)
        self.idStack.append(func_id)
        self.writeQuad('ERA', func_id, '0', '0')

    def funcCallParam(self):
        param, paramType, paramMemScope = self.popVar()
        calledFunc = self.peek(self.idStack)
        self.funcDir.validateParam(calledFunc, self.paramCounter, paramType)
        self.paramCounter += 1 # param counting starts at 0
        paramAddr = self.funcDir.getAddress(param, paramType, paramMemScope)
        aux = 'par'+str(self.paramCounter)
        self.writeQuad('PARAM', paramAddr, aux, '0')

    def funcCallEnd(self):
        func_id = self.idStack.pop()
        self.writeQuad('GOSUB', func_id, '0', '0')
        self.paramCounter = 0 # reset param counter
        # funcDir.validateFunctionSemantics(func_id)

    # -- ARRAYS --
    def accessArray(self, arrId, dimKey):
        idx, idxType, idxMem = self.popVar() # expresion que se leyo entre brackets [idx]
        idxAddr = self.funcDir.getAddress(idx, idxType, idxMem)
        if idxType != 'int':                  #TODO no estoy seguro si float tambien
            exceptions.fatalError("Se esperaba int para indexar arreglo, se recibió %s" % (idxType))
        arrVar = self.funcDir.getVariable(arrId)
        # verificacion de limites
        limit = arrVar[dimKey] - 1
        limitAddr = self.funcDir.getAddress(limit, 'int', 'const')
        zeroAddr = self.funcDir.getAddress(0, 'int', 'const')
        self.writeQuad('ver', idxAddr, zeroAddr, limitAddr) # checar si esta en rango
        # direccion base del arreglo como constante
        arrAddr = arrVar['address']
        baseAddr = self.funcDir.getAddress(arrAddr, 'int', 'const')
        # suma en un pointer temporal
        ptr = "pt"+str(self.temp)
        ptrAddr = self.funcDir.getAddress(ptr, 'ptr', 'temp')
        self.temp += 1
        self.writeQuad('+', baseAddr, idxAddr, ptrAddr) # sumar y poner en pointer
        # append pointer, tipo de dato es el mismo que el arreglo, no 'ptr'
        self.idStack.append(ptr)
        self.tpStack.append(idxType)
        self.memStack.append('temp')


    # -- RETORNA --
    def retorna(self):
        ret, retType, retMem = self.popVar()
        retAddr = self.funcDir.getAddress(ret, retType, retMem)
        gRetId = '&' + self.funcDir.scope
        globalRetVar = self.funcDir.getVariable(gRetId)
        if globalRetVar['type'] != retType:
            exceptions.fatalError("No se puede retornar '%s' en funcion '%s', se esparaba tipo '%s'" %(retType, self.funcDir.scope, globalRetVar['type']))
        self.writeQuad("=", retAddr, "0", globalRetVar['address'])

    # -- READ PRINT / QUACKIN QUACKOUT --
    def ioQuad(self, io):
        var, varType, varMemScope = self.popVar()
        varAddr = self.funcDir.getAddress(var, varType, varMemScope)
        self.writeQuad(io, varAddr, '0','0')

