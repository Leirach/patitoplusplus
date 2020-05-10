import sys

class CodeGenerator:
    def __init__(self, filename="patito"):
        self.f = open("out.obj", "w")
        self.code = []
        self.opStack = []
        self.idStack = []
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

    def buildExp(self):
        tok1 = self.opStack.pop()
        tok3 = self.idStack.pop()
        tok2 = self.idStack.pop()
        tok4 = "t"+str(self.temp)
        buf = "%s %s %s %s\n" % (tok1, tok2, tok3, tok4)
        self.idStack.append(tok4)
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
            sys.exit()
        else:
            self.dirFunc[id] = {"type": tipo}

    def endFunc(self):
        # calcular tamaño de todo self.temp tiene el count
        # liberar varTable, resetear temporales? idk
        self.temp = 1 # reset temp counter
        self.code.append("ENDFUNC\n")
        self.line+=1

    def funcCall(self, func_id):
        #check if functions exists in directory?
        self.idStack.append(func_id)
        buf = "ERA %s\n" % (func_id)
        self.code.append(buf)
        self.line+=1

    def funcCallParam(self):
        param = self.idStack.pop()
        self.paramCounter += 1 # starts @ 0
        buf = "PARAM %s par%d\n" % (param, self.paramCounter)
        self.code.append(buf)
        self.line+=1

    def funcCallEnd(self):
        func_id = self.idStack.pop()
        buf = "GOSUB %s\n" % (func_id)
        self.code.append(buf)
        self.line += 1
        self.paramCounter = 0 # reset param counter

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]    # this will get the last element of stack
        else:
            return None

