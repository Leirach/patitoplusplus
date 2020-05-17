import sys
import re 
import semanticTable as semantic
import functionDirectory as funcDir
class CodeGenerator:
    def __init__(self, filename="patito"):
        self.f = open("out.obj", "w")
        self.code = []
        self.opStack = []
        self.idStack = []
        self.tpStack = []
        self.funcStack = ['globals']
        self.gotoStack = []
        self.pendingLines = []
        self.dirFunc = {}
        self.paramCounter = 0
        self.forIds = []
        self.temp = 1
        self.line = 1

    def __del__(self):
        for line in self.code:
            self.f.write(line)
        self.f.close()


    # TODO 
    # se necesita tener nombre de función a la que pertenece :O
    def getVarType(self, p):
        functionName = self.funcStack.pop()
        print("functionName:", functionName)
        varType = funcDir.getVariableType(functionName, p)
        self.funcStack.append(functionName)
        return varType

    def getParamType(self, param):
        param = str(param)
        integers = re.compile('^[-+]?([1-9]\d*|0)$') #match int
        floats = re.compile('[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?') #match float
        chars = re.compile("^['][a-zA-Z][']+$") #match chars
        boolean = re.compile("^[true|false]+$")
        if integers.match(param):
            return 'int'
        elif floats.match(param):
            return 'float'
        elif chars.match(param):
            return 'char'
        elif boolean.match(param):
            return 'bool'
        else: 
            return self.getVarType(param) #falta validar tipo de ID??

    def registerVariable(self, id, varType):
        funcName = self.funcStack.pop()
        funcDir.addVar(funcName, id, varType)
        self.funcStack.append(funcName)

    def endVariableDeclaration(self):
        funcName = self.funcStack.pop()
        if(funcName == 'globals'):
            self.funcStack.append(funcName)

    def buildExp(self):
        op = self.opStack.pop()
        # pop ids from stack
        der = self.idStack.pop()
        derType = self.tpStack.pop()
        izq = self.idStack.pop()
        izqType = self.tpStack.pop()
        # get next temp var
        aux = "t"+str(self.temp)
        auxType = semantic.match(op, izqType, derType)
        if (auxType is None):
            print("Invalid operand %s for types %s and %s" % (op, izqType, derType))
            sys.exit()

        buf = "%s %s %s %s\n" % (op, izq, der, aux)
        self.idStack.append(aux)
        self.tpStack.append(auxType)
        self.temp += 1
        self.code.append(buf)
        print(self.code)
        self.line += 1

    def startIf(self):
        cond = self.idStack.pop()
        buf = "gotof %s" % (cond)
        self.code.append("if gotof\n")
        print(self.code)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.line += 1

    def elseIf(self):
        buf = "goto"
        self.code.append("else goto\n")
        self.line += 1
        print(self.code)
        self.endIf()
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line-1)

    def endIf(self):
        target = self.line
        lineNo = self.gotoStack.pop()
        buf = "%s %d\n" % (self.pendingLines.pop(), target)
        self.code[lineNo-1] = buf
        print(self.code)

    def whileStart(self):
        self.gotoStack.append(self.line)
        print(self.code)

    def whileDo(self):
        cond = self.idStack.pop()
        buf = "gotof %s" % (cond)
        self.code.append("while gotof\n")
        print(self.code)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.line += 1

    def whileEnd(self):
        lineNo = self.gotoStack.pop() - 1
        buf = "%s %d\n" % (self.pendingLines.pop(), self.line+1)
        self.code[lineNo] = buf
        retLine = self.gotoStack.pop()
        buf = "goto %d\n" % (retLine)
        self.code.append(buf)
        print(self.code)

    def forStart(self):
        val = self.idStack.pop()
        id = self.peek(self.idStack)
        self.forIds.append(id)
        buf = "%s %s %s %s\n" % ("=", val, " ", id)
        self.code.append(buf)
        self.line += 1
        self.gotoStack.append(self.line)
        print(self.code)

    def forDo(self):
        self.opStack.append("<=")
        self.buildExp()
        cond = self.idStack.pop()
        buf = "gotof %s" % (cond)
        self.code.append("loop gotof\n")
        print(self.code)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.line += 1

    def forEnd(self):
        id = self.forIds.pop()
        buf = "%s %s %d %s\n" % ('+', id, 1, id)
        self.code.append(buf)
        self.line += 1
        lineNo = self.gotoStack.pop() - 1
        buf = "%s %d\n" % (self.pendingLines.pop(), self.line+1)
        self.code[lineNo] = buf
        retLine = self.gotoStack.pop()
        buf = "goto %d\n" % (retLine)
        self.code.append(buf)
        print(self.code)

    def registerFunc(self, id, tipo): 
        if (self.dirFunc.get(id) is not None):
            #raise Exception("Función '%s' fue definida anteriormente." % (id))
            print("Función '%s' fue definida anteriormente." % (id))
            sys.exit()
        else:
            self.dirFunc[id] = {"type": tipo}
            self.funcStack.append(id)
            funcDir.addFunction(id, tipo)
    
    def registerFuncParams(self, id, tipo): 
        #hay un stack de ids de funciones???
        funcName =  self.funcStack.pop()
        funcDir.addParam(funcName, id ,tipo) #si no hay, hago la búsqueda directo en la última función registrada en el dir de funciones
        self.funcStack.append(funcName)
    
    def endFunc(self):
        # calcular tamaño de todo self.temp tiene el count
        # liberar varTable, resetear temporales? idk
        self.temp = 1 # reset temp counter
        self.code.append("ENDFUNC\n")
        self.line+=1
        self.endVariableDeclaration()
        print("END FUNC")

    def funcCall(self, func_id):
        #check if functions exists in directory? 
        self.idStack.append(func_id)
        buf = "ERA %s\n" % (func_id)
        self.code.append(buf)
        self.line+=1
        funcDir.addFunction(str(func_id)+"Call", "call")

    def funcCallParam(self):
        param = self.idStack.pop()
        if self.idStack:
            functionName = self.idStack.pop()
            self.paramCounter += 1 # starts @ 0
            buf = "PARAM %s par%d\n" % (param, self.paramCounter)
            self.code.append(buf)
            self.line+=1
            paramType = self.getParamType(param)
            funcDir.addParam(str(functionName)+"Call", param ,paramType)
            self.idStack.append(functionName)
        else:
            self.idStack.append(param)

    def funcCallEnd(self):
        func_id = self.idStack.pop()
        buf = "GOSUB %s\n" % (func_id)
        self.code.append(buf)
        self.line += 1
        self.paramCounter = 0 # reset param counter
        print("END FUNCCALL", func_id)
        funcDir.validateFunctionSemantics(func_id)
        


    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]    # this will get the last element of stack
        else:
            return None

