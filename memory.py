
offsets = {
    'global': 0,
    'local' : 10000,
    'temp' : 20000,
    'const' : 30000,
    'int' : 0,
    'float' : 1000,
    'bool' : 2000,
    'char' : 3000
}

class MemoryManager:
    def __init__(self):
        self.constants = { }
        self.temporals = { }
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
                'bool': 0
            },
            'temp': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
            'const': {
                'int': 0,
                'float': 0,
                'char': 0,
                'bool': 0
            },
        }

    def assignAddress(self, scope, tipo, size=1):
        addr = offsets[scope] + offsets[tipo] + self.counters[scope][tipo]
        self.counters[scope][tipo] += size
        return addr

    def getConstant(self, value, tipo):
        cte = self.constants.get(value)
        if cte is not None:
            return cte['addr']
        addr = self.assignAddress('const', tipo)
        self.constants.update({value: {'addr': addr, 'type': tipo}})
        return addr
        

    def getTemporal(self, value, tipo):
        temp = self.temporals.get(value)
        if temp is not None:
            return temp['addr']
        addr = self.assignAddress('temp', tipo)
        self.temporals.update({value: {'addr': addr, 'type': tipo}})
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
                'bool': 0
            }})

    def createConstTable(self):
        mem = []
        for key in self.constants:
            buf = "%s %s %s\n" %(self.constants[key]['addr'], key, self.constants[key]['type'])
            mem.append(buf)
        return mem