semanticTable = { 
    'int': {
        # deben estar todas las combinaciones en cada indice aunque este vacio
        # sino truena semanticTable[type1][type2]
        'int': {
            # lista de todos los operadores en patito++
            # no se tienen que agregar para cada combinacion,
            # si no estan match() regresa None
            '+': 'int',
            '-': 'int',
            '*': 'int',
            '/': 'int',
            '>': 'bool',
            '>=': 'bool',
            '<': 'bool',
            '<=': 'bool',
            '!=': 'bool',
            '==': 'bool',
            '&': None,
            '|': None,
            '$': None,
            '!': None,
            '^': None
        },
        'float': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            'GT': 'bool',
            '>=': 'bool',
            '<': 'bool',
            '<=': 'bool',
            '!=': 'bool',
            '==': 'bool',
        },
        'char': {},
        'bool': {},
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
    'float': {
        'int': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            'GT': 'bool',
            '>=': 'bool',
            '<': 'bool',
            '<=': 'bool',
            '!=': 'bool',
            '==': 'bool',
        },
        'float': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            'GT': 'bool',
            '>=': 'bool',
            '<': 'bool',
            '<=': 'bool',
            '!=': 'bool',
            '==': 'bool',
        },
        'char': { },
        'bool': { },
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
    'char': {
        'int': { },
        'float': { },
        'char': { },
        'bool': { },
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
    'bool': {
        'int': { },
        'float': { },
        'char': { },
        'bool': { 
            '&': 'bool',
            '|': 'bool'
        },
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
    'int[]': {
        'int': { },
        'float': { },
        'char': { },
        'bool': { },
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
    'float[]': {
        'int': { },
        'float': { },
        'char': { },
        'bool': { },
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
    'char[]': {
        'int': { },
        'float': { },
        'char': { },
        'bool': { },
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
    'bool[]': {
        'int': { },
        'float': { },
        'char': { },
        'bool': { },
        'int[]': {},
        'float[]': {},
        'bool[]': {},
        'char[]': {}
    },
}

def match(op, izqType, derType):
    return semanticTable[izqType][derType].get(op)

# semanticTable[TIPO1][TIPO2].get(OPERADOR) retorna None si no esta definido,
# None = no son compatibles
# print(semanticTable['bool']['bool'].get('+'))
