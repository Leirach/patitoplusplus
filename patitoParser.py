# === PARSER ===
# Parsing rules
import patitoLexer
import ply.yacc as yacc

tokens = patitoLexer.tokens

#stacks
opStack = []
idStack = []

def p_program_declaration(p):
    'program_declaration : PROGRAMA ID SEMICOLON declare_vars declare_func PRINCIPAL OPENPAR CLOSEPAR bloque'
    global programId
    programId = p[2]

def p_declare_vars(p):
    '''declare_vars : VAR vars
                    | empty'''

def p_vars(p):
    '''vars : tipo ID dimensions more_vars SEMICOLON vars
            | empty'''

def p_more_vars(p):
    '''more_vars : COMMA ID dimensions more_vars
                 | empty'''

def p_dimensions(p):
    '''dimensions : OPENBRAC CTEI CLOSEBRAC 
                  | OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRAC
                  | empty'''

def p_declare_func(p):
    '''declare_func : FUNCION tipo ID OPENPAR declare_func_params CLOSEPAR declare_vars bloque
                    | empty'''
                    
def p_declare_func_params(p):
    '''declare_func_params : tipo ID more_params
                           | empty'''

def p_more_params(p):
    '''more_params : COMMA tipo ID more_params
                  | empty'''

def p_tipo(p):
    '''tipo : INT 
            | FLOAT
            | CHAR
            | BOOL'''
    p[0] = p[1]

def p_bloque(p):
    'bloque : LCURLYB estatuto RCURLYB'

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
            | CTEC
            | TRUE
            | FALSE'''

# -- ID o acceso a arreglo --
def p_id(p):
    '''id : ID
          | ID OPENBRAC exp CLOSEBRAC
          | ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRAC'''

def p_desde(p):
    '''desde : DESDE ID ASSIGN exp HASTA exp HACER bloque'''

def p_mientras(p):
    '''mientras : MIENTRAS OPENPAR megaexp CLOSEPAR HAZ bloque'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("error")

parser = yacc.yacc()

while True:
    try:
        s = input('test > ')
    except EOFError:
        break
    parser.parse(s)
