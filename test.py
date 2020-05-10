# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc
import sys

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

# delcaracion, en patitoParser.py
# funcion void mifuncion () { quackout(variable); }

# llamada
# mifunc(123, abc);

# -- Funcion void --
def p_func_void(p):
    '''func_void : func_call_id OPENPAR func_call_params CLOSEPAR SEMICOLON'''

def p_func_call_id(p):
    'func_call_id : ID'
    code.funcCall(p[1])

#vcte para testear, deberia ser megaexp
#todo parsea de derecha a izquierda D:
def p_func_call_params(p):
    '''func_call_params : vcte more_call_params
                        | empty'''
    if (p[1] is not None):
        code.funcCallParam()

def p_more_call_params(p):
    '''more_call_params : COMMA vcte more_call_params
                        | empty'''
    if (p[1] is not None):
        code.funcCallParam()

def p_vcte(p):
    '''vcte : ID
            | CTEI
            | CTEF
            | CTEC
            | TRUE
            | FALSE'''
    p[0] = p[1]
    code.idStack.append(p[1])

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
