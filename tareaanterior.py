import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'SEMICOLON', 'COLON', 'COMMA',
    'PLUS', 'MINUS','TIMES','DIVIDE','EQUALS', 
    'GRATERTHAN', 'LESSTHAN', 'NOTEQUAL', 'LCURLYB', 'RCURLYB',
    'LPAREN','RPAREN','ID', 'CTEI', 'CTEF', 'CTES', 'QUOTE', 'STRING'
]

# Reserved 
reserved = {
    'program': 'PROGRAM',
    'int': 'INT',
    'float': 'FLOAT',
    'var' : 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT'
}

tokens += reserved.values()

# Tokens
t_GRATERTHAN = r'>'
t_LESSTHAN  = r'<'
t_NOTEQUAL  = r'<>'
t_LCURLYB   = r'{'
t_RCURLYB   = r'}'
t_SEMICOLON = r';'
t_COLON     = r':'
t_COMMA     = r','
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_QUOTE     = r'"'


def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEF(t):
    r'\d\.\d+'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING(t):
    r'"([^"\n]|(\\"))*"$'
    return t
 
# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

# Parsing rules

# dictionary of names
ids = { }
cte_i = { }
cte_d = { }

def p_program_declaration(t):
    'statement : PROGRAM ID SEMICOLON varss'
    ids["program"] = t[2]

def p_tipo_var(t):
    '''tipo : INT 
            | FLOAT'''

def p_varss(t):
    '''varss : VAR ID getvars COLON tipo SEMICOLON bloque 
            | empty '''

def p_getvars(t):
    '''getvars : COMMA ID getvars 
        | empty '''

def p_block_group(t):
    "bloque : LCURLYB estatuto RCURLYB"

def p_estatuto(t):
    '''estatuto : asignacion 
                | condicion 
                | escritura 
                | empty'''

def p_asignacion(t):
    "asignacion : ID EQUALS expression SEMICOLON"

#me falta poner el else opcional
def p_condicion(t):
    "condicion : IF LPAREN expression RPAREN bloque ifElse SEMICOLON"

def p_ifElse(t):
    '''ifElse : ELSE bloque 
              | empty'''

def p_escritura(t):
    "escritura : PRINT LPAREN attr RPAREN SEMICOLON"

def p_attr(t):
    '''attr : write printoptions'''

def p_write(t):
    '''write : STRING 
             | expression '''

def p_printoptions(t):
    '''printoptions : COMMA attr
                    | empty'''

def p_expression(t):
    '''expression : exp expoptions exp
                  | empty'''

def p_expoptions(t):
    '''expoptions : GRATERTHAN 
                  | LESSTHAN 
                  | NOTEQUAL'''

def p_exp(t):
    "exp : termino expp"

def p_expp(t):
    '''expp : exppp termino 
            | empty '''

def p_exppp(t):
    '''exppp : MINUS 
             | PLUS '''

def p_termino(t):
    "termino : factor fact"

def p_fact(t):
    '''fact : factt factor 
            | empty'''

def p_factt(t):
    '''factt : TIMES 
             | DIVIDE '''

def p_factor(t):
    '''factor : LPAREN expression RPAREN 
              | expp vcte '''
            
def p_vcte(t):
    '''vcte : ID 
            | CTEI 
            | CTEF '''

def p_empty(p):
    'empty :'
    pass


def p_error(t):
    print("Illegal character '%s' at %d" % (t.value,t.lineno))
    
parser = yacc.yacc()

while True:
    try:
        s = input('test > ')
    except EOFError:
        break
    parser.parse(s)
