class CodeGenerator:
    def __init__(self, filename="patito"):
        self.f = open("out.obj", "w")

    def __del__(self):
        self.f.close()

    def generate(self, tok1, tok2, tok3, tok4):
        buf = "%s %s %s %s\n" % (tok1, tok2, tok3, tok4)
        self.f.write(buf)

# =========== EXAMPLE ===========
# codeGen = CodeGenerator()
# codeGen.generate('A', 'B', 'C', 'D')
# codeGen.generate('A', 'B', '', 'C')
# codeGen.generate('PLUS', 'A', 'B', 'T1')
