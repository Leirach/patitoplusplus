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
        }
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
        }
        'CHAR': {},
        'BOOL': {}
    },
    'CHAR': {
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
        }
        'CHAR': {},
        'BOOL': {}
    }
}

print(semanticTable['INT']['INT'].get('KLJASD'))
