
import sys, getopt

class VirtualMachine:
    def __init__(self, file):
        f = open(file, "r")
        obj = f.read().splitlines()
        split = obj.index('')
        self.code = obj[:split]         # guardar cuadruplos
        self.code.insert(0,"")          # code index starts at 1
        obj = obj[split+1:]
        self.mem = {}
        self.reconstructMemory(obj)
        self.ip = 1                     # instruction pointer
        self.operations = {
            'goto' :self.goto,
            '+': self.sum,
            '-': self.subs,
            'print': self.print,
        }
        self.run()

    def reconstructMemory(self, obj):
        for line in obj:                # guardar en diccionario de memoria
            aux = line.split(':')
            self.mem[aux[0]] = int(aux[1])

    def run(self):
        while self.code[self.ip] != 'ENDFUNC 0 0':
            self.execute()
        return 0

    def execute(self):
        line = self.code[self.ip].split()
        op = line[0]
        self.operations[op](line[1], line[2], line[3])

    def goto(self, op1, op2, op3):
        self.ip = int(op1)

    def sum(self, op1, op2, op3):
        self.mem[op3] = self.mem[op1] + self.mem[op2]
        self.ip += 1

    def subs(self, op1, op2, op3):
        self.mem[op3] = self.mem[op1] - self.mem[op2]
        self.ip += 1

    def print(self, op1, op2, op3):
        print(self.mem[op1])
        self.ip += 1

try:
    obejota = sys.argv[1]
except IndexError:
    print ('Uso: python VirtualMachine.py <obejota.obj>')

vm = VirtualMachine(obejota)
