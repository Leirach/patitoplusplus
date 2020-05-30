
import sys, getopt
memEmpty = {
    'global': {
        'int': [],
        'float': [],
        'char': [],
        'bool': []
    },
    'local': {
        'int': [],
        'float': [],
        'char': [],
        'bool': [],
    },
    'temp': {
        'int': [],
        'float': [],
        'char': [],
        'bool': [],
        'ptr' : []
    },
    'const': {
        'int': [],
        'float': [],
        'char': [],
        'bool': []
    }
}

class VirtualMachine:
    def __init__(self, file):
        f = open(file, "r")
        obj = f.read().splitlines()
        split = obj.index('')
        self.code = obj[:split]         # guardar cuadruplos
        self.code.insert(0,"")          # code index starts at 1
        obj = obj[split+1:]
        self.mem = memEmpty
        self.funcdir = {}
        self.reconstructMemory(obj)
        self.ip = 1                     # instruction pointer
        self.operations = {
            'goto' :self.goto,
            'gotof': self.gotof,
            '=': self.assign,
            '+': self.sum,
            '-': self.subs,
            '*': self.mult,
            '/': self.div,
            '>': self.gt,
            '>=': self.gte,
            '<': self.lt,
            '<=': self.lte,
            '!=': self.neq,
            '==': self.eq,
            '&': self.op_and,
            '|': self.op_or,
            # '$': self.determ,
            # '!': self.transpose,
            # '^': self.inverse,
            'ERA': self.era,
            'PARAM': self.param,
            'GOSUB': self.gosub,
            'ENDFUNC': self.endfunc,
            # 'ver': self.verify,
            'print': self.print,
            'read': self.read,
        }
        self.run()

    def offsetMemory(self, addr):
        # offset de scope
        scope = tipo = ''
        if addr < 10000:
            scope = 'global'
            addr -= 1 # la primer direccion global esta en 1, para no confundir con el padding de 0's
        elif addr < 20000:
            scope = 'local'
            addr = addr - 10000
        elif addr < 30000:
            scope = 'temp'
            addr = addr - 20000
        else:
            scope = 'const'
            addr = addr - 30000
        # offset de tipo
        if addr < 2000:         # int
            tipo = 'int'
            # addr no cambia
        elif addr < 4000:       # float
            tipo = 'float'
            addr = addr - 2000
        elif addr < 6000:       # bool
            tipo = 'bool'
            addr = addr - 4000
        else:                   # char
            tipo = 'char'
            addr = addr - 6000
        return addr, scope, tipo

    def malloc(self, scope, sizes):
        types = ['int', 'float', 'char', 'bool']
        for i in len(sizes):
            if sizes[i] == 0:
                sizes[i] = 1
            self.mem[scope][types[i]] = [0] * sizes[i]

    def memSet(self, addr, value):
        addr = int(addr)
        addr, scope, tipo = self.offsetMemory(addr)
        if tipo == 'int':
            value = int(value)
        elif tipo == 'float':
            value = float(value)
        elif tipo == 'bool':
            value = value == 'true'
        # por si no hay espacio en el arreglo
        if len(self.mem[scope][tipo]) <= addr:
            self.mem[scope][tipo].insert(addr, value)
        else:
            self.mem[scope][tipo][addr] = value

    def memGet(self, addr):
        addr = int(addr)
        addr, scope, tipo = self.offsetMemory(addr)
        return self.mem[scope][tipo][addr] # accesos => dicc dicc arreglo

    def reconstructMemory(self, obj): # los diccionarios son nacos
        split = obj.index('')
        funcs = obj[:split]
        memory = obj[split+1:]
        idx = 0
        while idx < len(funcs):
            identifier = funcs[idx].split()
            local = funcs[idx+1].split()
            local = list(map(int, local[1:]))
            temp = funcs[idx+1].split()
            temp = list(map(int, temp[1:]))
            func = {
                identifier[0] : {'goto': int(identifier[2]), 'local': local, 'temp': temp}
            }
            self.funcdir.update(func)

        sizes = memory[0].split()
        self.malloc('global', sizes[1:])
        sizes = memory[1].split()
        self.malloc('const', sizes[1:])
        memory = memory[2:]
        for line in memory:
            aux = line.split()
            self.memSet(int(aux[0]), aux[1])

    def run(self):
        while self.code[self.ip] != 'ENDFUNC 0 0 0':
            line = self.code[self.ip].split()
            op = line[0]
            self.operations[op](line[1], line[2], line[3])
        return 0

    # operaciones en ejecucion
    def goto(self, op1, op2, op3):
        self.ip = int(op1)

    def gotof(self, op1, op2, op3):
        if (not self.memGet(op1)):
            self.ip = int(op2)
        else:
            self.ip += 1

    def assign(self, op1, op2, op3):
        temp = self.memGet(op1)
        self.memSet(op3, temp)
        self.ip += 1

    # Aritmeticos
    def sum(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 + temp2)
        self.ip += 1
    def subs(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 - temp2)
        self.ip += 1
    def mult(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 * temp2)
        self.ip += 1
    def div(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 / temp2)
        self.ip += 1

    # comparaciones
    def gt(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 > temp2)
        self.ip += 1
    def gte(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 >= temp2)
        self.ip += 1
    def lt(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 < temp2)
        self.ip += 1
    def lte(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 <= temp2)
        self.ip += 1
    def neq(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 != temp2)
        self.ip += 1
    def eq(self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 == temp2)
        self.ip += 1

    # logicos booleanos
    def op_and (self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 and temp2)
        self.ip += 1
    def op_or (self, op1, op2, op3):
        temp1 = self.memGet(op1)
        temp2 = self.memGet(op2)
        self.memSet(op3, temp1 or temp2)
        self.ip += 1

    # funciones
    def era(self, op1, op2, op3):
        # entrar a funcion
        pass
    
    def param(self, op1, op2, op3):
        #asignar parametro a funcion
        pass

    def gosub(self, op1, op2, op3):
        # ir a funcion en func dir
        pass

    def endfunc(self, op1, op2, op3):
        # cambiar de contexto al anterior
        # si ya esta vacio el stack / se acaba main terminar ejecucion
        pass
    # otros
    def print(self, op1, op2, op3):
        print(self.memGet(op1))
        self.ip += 1
    
    def read(self, op1, op2, op3):
        temp = input()
        self.memSet(op1, temp)
        self.ip += 1

try:
    obejota = sys.argv[1]
except IndexError:
    print ('Uso: python VirtualMachine.py <obejota.obj>')

vm = VirtualMachine(obejota)
