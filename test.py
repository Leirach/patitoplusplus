# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import ply.yacc as yacc

tokens = patitoLexer.tokens

#stacks
opStack = []
idStack = []

def p_program_declaration(p):
    'program_declaration : PROGRAMA ID SEMICOLON declare_vars declare_func PRINCIPAL OPENPAR CLOSEPAR bloque'

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

def p_bloque(p):
    'bloque : LCURLYB estatuto RCURLYB'

def p_estatuto(p):
    '''estatuto : empty'''

def p_tipo(p):
    '''tipo : INT 
            | FLOAT
            | CHAR
            | BOOL'''
    p[0] = p[1]

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
