# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

# -- Expresiones

def p_exp(p):
    '''exp : termino
           | exp sums termino'''
    nextOp = code.peek(code.opStack) 
    if (nextOp == '+' or nextOp == '-'):
        code.generate()
    elif nextOp is not None:
        print("pending operation @exp", nextOp)

def p_termino(p):
    '''termino : factor
               | termino multdiv factor'''
    nextOp = code.peek(code.opStack) 
    if (nextOp == '*' or nextOp == '/'):
        code.generate()
    elif nextOp is not None:
        print("pending operation @termino", nextOp)

def p_factor(p):
    '''factor : vcte
              | openpar exp closepar'''

def p_vcte(p):
    '''vcte : ID
            | CTEI'''
    p[0] = p[1]
    code.idStack.append(p[1])

# -- Operadores --

def p_sums(p):
    '''sums : MINUS 
            | PLUS'''
    p[0] = p[1]
    code.opStack.append(p[1])
    
def p_multdiv(p):
    '''multdiv : TIMES
               | DIVIDE'''
    p[0] = p[1]
    code.opStack.append(p[1])

# agregar fondo falso a opstack
def p_openpar(p): 
    'openpar : OPENPAR'
    code.opStack.append(p[1])

# quitar fondo falso
def p_closepar(p): 
    'closepar : CLOSEPAR'
    code.opStack.pop()


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
    parser.parse(s, debug=0)
