semanticTable = { 
    'int': {
        'int': {
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
            '|': None
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
        'CHAR': {},
        'bool': {}
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
        'CHAR': { },
        'bool': { }
    },
    'char': {
        'int': { },
        'float': { },
        'CHAR': { },
        'bool': { }
    },
    'bool': {
        'int': { },
        'float': { },
        'CHAR': { },
        'bool': { 
            '&': 'bool',
            '|': 'bool'
        }
    }
}

def match(op, izqType, derType):
    return semanticTable[izqType][derType].get(op)

# semanticTable[TIPO1][TIPO2].get(OPERADOR) retorna None si no esta definido,
# None = no son compatibles
# print(semanticTable['bool']['bool'].get('+'))
