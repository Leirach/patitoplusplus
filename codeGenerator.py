class CodeGenerator:
    def __init__(self, filename="patito"):
        self.f = open("out.obj", "w")
        self.opStack = []
        self.idStack = []
        self.cont = 1

    def __del__(self):
        self.f.close()

    def buildExp(self):
        tok1 = self.opStack.pop()
        tok3 = self.idStack.pop()
        tok2 = self.idStack.pop()
        tok4 = "t"+str(self.cont)
        buf = "%s %s %s %s\n" % (tok1, tok2, tok3, tok4)
        self.idStack.append(tok4)
        self.cont += 1
        print(buf)
        self.f.write(buf)

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]    # this will get the last element of stack
        else:
            return None

# =========== EXAMPLE ===========
# codeGen = CodeGenerator()
# codeGen.generate('A', 'B', 'C', 'D')
# codeGen.generate('A', 'B', '', 'C')
# codeGen.generate('PLUS', 'A', 'B', 'T1')
