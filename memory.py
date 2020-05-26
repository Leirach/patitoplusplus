
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

class MemoryManager:
    def __init__(self):
        self.constants = { }
        self.temporals = { }
        self.memory = {
            'const': { },
            'temp': { }
        }
        self.counters = {
            'global': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            'local': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
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
                'bool': 0
            },
        }

    def assignAddress(self, scope, tipo, dim1=None, dim2=None):
        size = 0
        if dim1 is not None:
            size = dim1
        if dim2 is not None:
            size *= dim2
        size += 1
        addr = offsets[scope] + offsets[tipo] + self.counters[scope][tipo]
        self.counters[scope][tipo] += size
        return addr

    def getAddress(self, value, tipo, scope):
        aux = self.memory[scope].get(value)
        if aux is not None:
            return aux['addr']
        addr = self.assignAddress(scope, tipo)
        self.memory[scope].update({value: {'addr': addr, 'type': tipo}})
        return addr

    def reset(self):
        self.temporals = { }
        self.counters.update( 
            {'local': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            'temp': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0,
                'ptr' : 0
            }})

    def createConstTable(self):
        mem = []
        for key in self.memory['const']:
            buf = "%s %s %s\n" %(self.memory['const'][key]['addr'], key, self.memory['const'][key]['type'])
            mem.append(buf)
        return mem