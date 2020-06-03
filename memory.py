
offsets = {
    'global': 1,
    'local' : 10000,
    'temp' : 20000,
    'const' : 30000,
    'int' : 0,
    'float' : 2000,
    'bool' : 4000,
    'char' : 6000,
    'ptr' : 8000
}

TYPES = ['int', 'float', 'char', 'bool', 'ptr'] # para iterar diccionarios

class MemoryManager:
    def __init__(self):
        self.memory = {
            'const': { },
            'temp': { }
        }
        self.counters = {
            'global': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'ptr': 0
            },
            'local': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'ptr': 0
            },
            'temp': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'ptr' : 0
            },
            'const': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'ptr': 0
            },
        }

    # Crea una nueva dirección basada en el scope, el tipo
    # y la memoria ocupada previamente en el mismo
    def assignAddress(self, scope, tipo, dim1=None, dim2=None):
        size = 0
        if dim1 is not None:
            size = dim1
        if dim2 is not None: # siempre que hay dim2 hay dim1
            size *= dim2
        size += 1
        addr = offsets[scope] + offsets[tipo] + self.counters[scope][tipo]
        self.counters[scope][tipo] += size
        return addr

    # Trae la dirección de la variable enviada como parámetro
    # si no tiene dirección la crea
    def getAddress(self, value, tipo, scope):
        aux = self.memory[scope].get(value)
        if aux is not None:
            return aux['addr']
        addr = self.assignAddress(scope, tipo)
        self.memory[scope].update({value: {'addr': addr, 'type': tipo}})
        return addr

    def reset(self):
        self.memory['temp'] = { }
        ret = {
            'local': self.counters['local'].copy(),
            'temp': self.counters['temp'].copy()
        }
        self.counters.update( 
            {'local': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'ptr': 0
            },
            'temp': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'ptr' : 0
            }})
        return ret

    def createConstTable(self):
        mem = []
        temp = []
        temp2 = []
        for key in TYPES:
            temp.append(str(self.counters['global'][key]))
            temp2.append(str(self.counters['const'][key]))
        mem.append('global ' + " ".join(temp) + '\n')
        mem.append('const ' + " ".join(temp2) + '\n')
        for key in self.memory['const']:
            val = key
            if self.memory['const'][key]['type'] == 'bool':
                val = 1 if key == 'true' else 0
            buf = "%s %s\n" %(self.memory['const'][key]['addr'], val)
            mem.append(buf)
        return mem
