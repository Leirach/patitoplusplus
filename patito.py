import ply.lex as lex
import ply.yacc as yacc

# === LEXER ===
tokens = [
    'SEMICOLON', 'COLON', 'COMMA',
    'PLUS', 'MINUS','TIMES','DIVIDE', 'ASSIGN',
    'GTE', 'LTE', 'NEQ', 'EQ', 'GT', 'LT', 'AND', 'OR',
    'LCURLYB', 'RCURLYB', 'OPENPAR', 'CLOSEPAR', 'OPENBRAC', 'CLOSEBRAC',
    'ID', 'CTEI', 'CTEF', 'CTES', 'CTEC'
]

# Reserved 
reserved = {
    'programa': 'PROGRAMA',
    'principal': 'PRINCIPAL',
    'var' : 'VAR',
    'funcion': 'FUNCION',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'si': 'SI',
    'entonces': 'ENTONCES',
    'sino': 'SINO',
    'mientras': 'MIENTRAS',
    'haz': 'HAZ',
    'desde': 'DESDE',
    'hasta': 'HASTA',
    'hacer': 'HACER',
    'quackin': 'LEE',
    'quackout': 'ESCRIBE',
    'retorno': 'RETORNO'
}

tokens += reserved.values()

# Tokens
t_AND       = r'&'
t_OR     = r'\|'
t_GT        = r'>'
t_GTE       = r'>='
t_LT        = r'<'
t_LTE       = r'<='
t_NEQ       = r'!='
t_EQ        = r'=='
t_LCURLYB   = r'{'
t_RCURLYB   = r'}'
t_OPENPAR   = r'\('
t_CLOSEPAR  = r'\)'
t_OPENBRAC  = r'\['
t_CLOSEBRAC = r'\]'
t_SEMICOLON = r';'
t_COLON     = r':'
t_COMMA     = r','
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r'='


def t_CTEF(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
def t_CTEC(t):
    r"'.'"
    return t
    
def t_CTES(t):
    r'"([^"\n]|(\\"))*"$'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved.get(t.value, 'ID')
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

# === PARSER ===
# Parsing rules

# dictionary of names
ids = { }
cte_i = { }
cte_d = { }

def p_tipo(p):
    '''tipo : INT 
            | FLOAT
            | CHAR'''

def p_program_declaration(p):
    'program_declaration : PROGRAMA ID SEMICOLON declare_vars declare_func PRINCIPAL OPENPAR CLOSEPAR bloque'
    ids["program"] = t[2]

def p_dimensions(p):
    '''dimensions : OPENBRAC CTEI CLOSEBRAC 
                  | OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRAC
                  | empty'''

def p_declare_vars(p):
    '''declare_vars : VAR vars
                    | empty'''

def p_vars(p):
    '''vars : tipo ID dimensions getvars COLON SEMICOLON vars
            | empty '''

def p_getvars(p):
    '''getvars : COMMA ID dimensions getvars 
               | empty '''

def p_declare_func(p):
    '''declare_func : FUNCION tipo ID OPENPAR declare_func_params CLOSEPAR declare_vars bloque'''

def p_declare_func_params(p):
    '''declare_func_params : tipo ID more_params
                          | empty'''

def p_more_params(p):
    '''more_params : COMMA tipo ID
                  | empty'''

def p_block_group(p):
    'bloque : LCURLYB estatuto RCURLYB'

#
def p_estatuto(p):
    '''estatuto : asignacion 
                | condicion 
                | func_void
                | retorno
                | escribe
                | lee 
                | desde
                | mientras
                | empty'''

# -- ID o acceso a arreglo --
def p_id(p):
    '''id : ID
          | ID OPENBRAC exp CLOSEBRAC
          | ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRAC'''

# -- Asignacion --
def p_asignacion(p):
    "asignacion : id ASSIGN megaexp SEMICOLON"

# -- Condicion --
def p_condicion(p):
    "condicion : SI OPENPAR megaexp CLOSEPAR ENTONCES bloque bloque_sino"

def p_bloque_sino(p):
    '''bloque_sino : SINO bloque 
              | empty'''

# -- Funcion void --
def p_func_call_params(p):
    '''func_call_params : megaexp more_call_params
                       | empty'''

def p_more_call_params(p):
    '''more_call_params : COMMA megaexp
                        | empty'''

def p_func_void(p):
    '''func_void : ID OPENPAR CLOSEPAR func_call_params SEMICOLON'''

# -- Escribir --
def p_escribe(p):
    "escribe : ESCRIBE OPENPAR print_options CLOSEPAR SEMICOLON"

def p_print_options(p):
    '''print_options : CTES more_print
                     | megaexp more_print'''

def p_more_print(p):
    '''more_print : COMMA CTES
                   | COMMA megaexp
                   | empty'''

# -- Leer --
def p_lee(p):
    '''lee : LEE OPENPAR ID read_more CLOSEPAR SEMICOLON'''

def p_read_more(p):
    '''read_more : COMMA ID read_more
                 | empty'''

# -- Retorno --
def p_retorno(p):
    'retorno : RETORNO OPENPAR megaexp CLOSEPAR'

# -- Operadores --
def p_boolean_op(p):
    '''blooean_op : OR 
                  | AND'''

def p_logical_op(p):
    '''logical_op : GT
                  | GTE
                  | LT
                  | LTE
                  | NEQ
                  | EQ'''

def p_sums(p):
    '''sums : MINUS 
            | PLUS '''

def p_multdiv(p):
    '''multdiv : TIMES 
               | DIVIDE '''

# -- Expresiones
def p_megaexp(p):
    '''megaexp : superexp
               | superexp blooean_op megaexp'''

def p_superexp(p):
    '''superexp : exp
                | exp logical_op superexp'''

def p_exp(p):
    '''exp : termino
            | termino sums exp'''

def p_termino(p):
    '''termino : factor
               | factor multdiv factor'''

def p_factor(p):
    '''factor : vcte
              | OPENPAR megaexp CLOSEPAR'''
            
def p_vcte(p):
    '''vcte : id
            | CTEI
            | CTEF
            | CTEC'''

def p_desde(p):
    '''desde : DESDE ID ASSIGN exp HASTA exp HACER bloque'''

def p_mientras(p):
    '''mientras : MIENTRAS OPENPAR megaexp CLOSEPAR HAZ bloque'''

def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()

while True:
    try:
        s = input('test > ')
    except EOFError:
        break
    parser.parse(s)
