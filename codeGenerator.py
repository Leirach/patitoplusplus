import sys
import re 
import semanticTable as semantics
import functionDirectory as fm

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
        for line in self.code:
            self.f.write(line)
        self.f.close()

    # se necesita tener nombre de función a la que pertenece, yasya
    def getVarType(self, p):
        return self.funcDir.getVariableType(None, p) #default scope

    def buildExp(self):
        op = self.opStack.pop()
        # pop ids from stack
        der = self.idStack.pop()
        derType = self.tpStack.pop()
        derMemScope = self.memStack.pop()
        izq = self.idStack.pop()
        izqType = self.tpStack.pop()
        izqMemScope = self.memStack.pop()
        # get next temp var
        aux = "t"+str(self.temp)
        auxType = semantics.match(op, izqType, derType)
        if auxType is None:
            print("Invalid operand %s for types %s and %s" % (op, izqType, derType))
            sys.exit()

        izqAddr = self.funcDir.getAddress(izq, izqMemScope, izqType)
        derAddr = self.funcDir.getAddress(der, derMemScope, derType)
        auxAddr = self.funcDir.getAddress(aux, 'temp', auxType)
        buf = "%s %s %s %s\n" % (op, izqAddr, derAddr, auxAddr)
        self.code.append(buf)
        self.idStack.append(aux)
        self.tpStack.append(auxType)
        self.memStack.append('temp')
        self.temp += 1
        self.line += 1
        print(self.code)

    # TODO incompleto
    def buildUnaryExp(self):
        op = self.opStack.pop()
        var = self.idStack.pop()
        if op == '-':
            self.idStack.append(op+var)
        elif op == '+':
            self.idStack.append(var)
        else:
            self.idStack.append(op+var)

    def ifStart(self):
        cond = self.idStack.pop()
        buf = "gotof %s" % (cond)
        self.code.append("if gotof\n")
        print(self.code)
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line)
        self.line += 1

    def ifElse(self):
        buf = "goto"
        self.code.append("else goto\n")
        self.line += 1
        print(self.code)
        self.ifEnd()
        self.pendingLines.append(buf)
        self.gotoStack.append(self.line-1)

    def ifEnd(self):
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

    def registerVariable(self, id, varType):
        self.funcDir.registerVariable(id, varType)

    def registerFunc(self, functionName, functionType):
        if functionName == 'principal':
            self.code[0] = "goto %d\n" %(self.line)
            self.line += 1
        self.funcDir.registerFunc(functionName, functionType)

    def registerFuncParams(self, paramId, paramType):
        self.funcDir.registerFuncParams(paramId, paramType) 

    def endFunc(self):
        # calcular tamaño de todo, self.temp tiene el count
        self.temp = 1 # reset temp counter
        self.code.append("ENDFUNC\n")
        self.line += 1
        self.funcDir.endFunc()
        print("END FUNC")

    def funcCallStart(self, func_id):
        #check if functions exists in directory?
        self.funcDir.callFunction(func_id)
        self.idStack.append(func_id)
        buf = "ERA %s\n" % (func_id)
        self.code.append(buf)
        self.line+=1

    def funcCallParam(self):
        param = self.idStack.pop()
        paramType = self.tpStack.pop()
        paramMemScope = self.memStack.pop()
        calledFunc = self.peek(self.idStack)
        self.funcDir.validateParam(calledFunc, self.paramCounter, paramType)
        self.paramCounter += 1 # starts @ 0
        paramAddr = self.funcDir.getAddress(param, paramMemScope, paramType)
        buf = "PARAM %s par%d\n" % (paramAddr, self.paramCounter)
        self.code.append(buf)
        self.line += 1

    def funcCallEnd(self):
        func_id = self.idStack.pop()
        buf = "GOSUB %s\n" % (func_id)
        self.code.append(buf)
        self.line += 1
        self.paramCounter = 0 # reset param counter
        print("END FUNCCALL", func_id)
        # funcDir.validateFunctionSemantics(func_id)
    
    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]    # this will get the last element of stack
        else:
            return None

