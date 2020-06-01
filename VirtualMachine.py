import sys, getopt
TYPES = ['int', 'float', 'char', 'bool'] # para iterar diccionarios
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
        self.mem = memEmpty
        self.contextStack = []
        self.arStack = [{'func_id': 'principal', 'params': []}] # Activation Record Stack
        self.funcdir = {}
        self.ip = 1                     # instruction pointer
        self.operations = {
            'GOTO' :self.goto,
            'GOTOF': self.gotof,
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
            'PRINT': self.print,
            'READ': self.read,
        }
        self.readCode(file)
        self.running = True
        self.run()

    # -- LECTURA DE CODIGO FUENTE --
    def readCode(self, file):
        f = open(file, "r")
        obj = f.read().splitlines()     # pasa el codigo a un arreglo de lineas
        div = obj.index('')             # primera division entre -> codigo / funcs mem
        self.code = obj[:div]           # guardar cuadruplos
        self.code.insert(0,"")          # para gotos, indice 1
        obj = obj[div+1:]               # quitar cuadruplos
        div = obj.index('')             # dividir otra vez -> funcs / mem
        funcs = obj[:div]
        self.reconstructFunctions(funcs) # reconstruir funciones
        mem = obj[div+1:]
        self.reconstructMemory(mem)      # reconstruir memoria
    
    def reconstructFunctions(self, funcs):
        while len(funcs) > 0:
            signature = funcs.pop(0).split() # [id, goto, paramCount]
            params = []
            for _i in range(0, int(signature[2])):
                par = funcs.pop(0).split()
                params.append(int(par[1]))
            local = funcs.pop(0).split()
            temp = funcs.pop(0).split()
            func = {
                signature[0] : {
                    'goto': int(signature[1]),          # goto line
                    'local': local[1:],                 # local mem sizes
                    'temp': temp[1:],                   # temp mem sizes
                    'paramCount': int(signature[2]),    # param count
                    'params': params,                   # param address list
                }
            }
            self.funcdir.update(func)

    def reconstructMemory(self, memory): # los diccionarios son nacos
        sizes = memory[0].split()
        self.malloc('global', sizes[1:])
        sizes = memory[1].split()
        self.malloc('const', sizes[1:])
        memory = memory[2:]
        for line in memory:
            aux = line.split()
            self.memSet(int(aux[0]), aux[1])

    # -- MANEJO DE MEMORIA --
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
        sizes = list(map(int, sizes))
        for i in range(0, len(sizes)):
            if sizes[i] > 0:
                self.mem[scope][TYPES[i]] = [0] * sizes[i]

    def memSet(self, addr, value):
        addr = int(addr)
        addr, scope, tipo = self.offsetMemory(addr)
        if tipo == 'int':
            value = int(value)
        elif tipo == 'float':
            value = float(value)
        elif tipo == 'bool':
            value = bool(value)
        self.mem[scope][tipo][addr] = value

    def memGet(self, addr):
        addr = int(addr)
        addr, scope, tipo = self.offsetMemory(addr)
        return self.mem[scope][tipo][addr] # accesos => dicc dicc arreglo

    # -- EJECUCION --
    def run(self):
        while self.running:
            line = self.code[self.ip].split()
            op = line[0]
            self.operations[op](line[1], line[2], line[3])
        return 0

    # gotos
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
        print(self.memGet(op3))
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

    # funciones - 4 horsemen of the apocalypse
    def era(self, op1, op2, op3):
        self.arStack.append({'func_id': op1, 'params': []})
        self.ip += 1

    def param(self, op1, op2, op3):
        activationRecord = self.arStack[-1]             # apuntador a ultimo llamada de funcion
        param_value = self.memGet(op1)
        activationRecord['params'].append(param_value)
        self.ip += 1

    def gosub(self, op1, op2, op3):
        # se guarda una copia de la memoria local y temporal
        context = {
            'mem': {'local': self.mem['local'].copy(), 'temp': self.mem['temp'].copy()},
            'ip': self.ip + 1
        }
        self.contextStack.append(context)
        activationRecord = self.arStack.pop()
        func = self.funcdir[ activationRecord['func_id'] ] # entrada en dir de func
        self.malloc('local', func['local'])
        self.malloc('temp', func['temp'])
        for i in range(0, func['paramCount']):
            addr = func['params'][i]
            val = activationRecord['params'][i]
            self.memSet(addr, val)
        self.ip = self.funcdir[op1]['goto']

    def endfunc(self, op1, op2, op3):
        # cambiar de contexto al anterior
        if len(self.contextStack) == 1:
            self.running = False
        else:
            prevContext = self.contextStack.pop()
            for key in TYPES:
                self.mem['local'][key] = prevContext['mem']['local'][key]
                self.mem['temp'][key] = prevContext['mem']['temp'][key]
            self.ip = prevContext['ip']

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
