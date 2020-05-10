# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc
import sys

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

# funcion void mifuncion () { quackout(variable); }

def p_declare_func(p):
    '''declare_func : FUNCION func_id OPENPAR declare_func_params CLOSEPAR bloque'''
                   #| empty'''
    code.endFunc()

def p_func_id(p):
    '''func_id : tipo ID
               | VOID ID'''
    code.registerFunc(id=p[2], tipo=p[1])

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
    'bloque : LCURLYB estatutos_rec RCURLYB'

def p_estatutos_rec(p):
    '''estatutos_rec : estatuto estatutos_rec
                     | empty''' 

def p_estatuto(p):
    '''estatuto : escribe
                | lee '''

# -- Escribir --
def p_escribe(p):
    "escribe : QUACKOUT OPENPAR print_options CLOSEPAR SEMICOLON"

def p_print_options(p):
    '''print_options : CTES more_print
                     | ID more_print'''

def p_more_print(p):
    '''more_print : COMMA CTES
                  | COMMA ID
                  | empty'''

# -- Leer --
def p_lee(p):
    '''lee : QUACKIN OPENPAR ID read_more CLOSEPAR SEMICOLON'''

def p_read_more(p):
    '''read_more : COMMA ID read_more
                 | empty'''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("error")
    
parser = yacc.yacc()

while True:
    try:
        s = input('test > ')
        if s == '$':
            sys.exit()
    except EOFError:
        break
    parser.parse(s)
