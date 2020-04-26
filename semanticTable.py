semanticTable = { 
    'INT': {
        'INT': {
            'PLUS': 'INT',
            'MINUS': 'INT',
            'TIMES': 'INT',
            'DIVIDE': 'INT',
            'GT': 'BOOL',
            'GTE': 'BOOL',
            'LT': 'BOOL',
            'LTE': 'BOOL',
            'NEQ': 'BOOL',
            'EQ': 'BOOL',
            'AND': None,
            'OR': None
        },
        'FLOAT': {
            'PLUS': 'FLOAT',
            'MINUS': 'FLOAT',
            'TIMES': 'FLOAT',
            'DIVIDE': 'FLOAT',
            'GT': 'BOOL',
            'GTE': 'BOOL',
            'LT': 'BOOL',
            'LTE': 'BOOL',
            'NEQ': 'BOOL',
            'EQ': 'BOOL',
        },
        'CHAR': {},
        'BOOL': {}
    },
    'FLOAT': {
        'INT': {
            'PLUS': 'FLOAT',
            'MINUS': 'FLOAT',
            'TIMES': 'FLOAT',
            'DIVIDE': 'FLOAT',
            'GT': 'BOOL',
            'GTE': 'BOOL',
            'LT': 'BOOL',
            'LTE': 'BOOL',
            'NEQ': 'BOOL',
            'EQ': 'BOOL',
        },
        'FLOAT': {
            'PLUS': 'FLOAT',
            'MINUS': 'FLOAT',
            'TIMES': 'FLOAT',
            'DIVIDE': 'FLOAT',
            'GT': 'BOOL',
            'GTE': 'BOOL',
            'LT': 'BOOL',
            'LTE': 'BOOL',
            'NEQ': 'BOOL',
            'EQ': 'BOOL',
        },
        'CHAR': { },
        'BOOL': { }
    },
    'CHAR': {
        'INT': { },
        'FLOAT': { },
        'CHAR': { },
        'BOOL': { }
    },
    'BOOL': {
        'INT': { },
        'FLOAT': { },
        'CHAR': { },
        'BOOL': { 
            'AND': 'BOOL',
            'OR': 'BOOL'
        }
    }
}

# semanticTable[TIPO1][TIPO2].get(OPERADOR) retorna None si no esta definido
# es decir no son compatibles
# print(semanticTable['BOOL']['BOOL'].get('PLUS'))
