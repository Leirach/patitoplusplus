# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc
import sys

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

# mientras (A>B) haz { C+D }
# desde pedrito = 3 hasta 5+5 hacer { A+B }

# -- Desde --
def p_desde(p):
    '''desde : DESDE forId ASSIGN exp hasta exp hacer bloque'''
    code.forEnd()

def p_forId(p):
    'forId : ID'
    code.idStack.append(p[1])

def p_desde_hasta(p):
    'hasta : HASTA'
    code.forStart()

def p_desde_hacer(p):
    'hacer : HACER'
    code.forDo()

# desde i = 1 hasta 10 hacer { }
# = 1 _ i // HASTA
#resolver exp t1// HACER poner migajita
#<= i t1 t2 // comparacion
#gotof t2 _ // meter inclomento en pendingLines
#+ A B t3
#+ i 1 i //al final del for
#goto 2

def p_bloque(p):
    'bloque : LCURLYB estatutos_rec RCURLYB'

def p_estatutos_rec(p):
    '''estatutos_rec : estatuto estatutos_rec
                     | empty''' 

def p_estatuto(p):
    '''estatuto : desde
                | megaexp'''


# -- Operadores --
def p_boolean_op(p):
    '''boolean_op : OR 
                  | AND'''
    p[0] = p[1]
    code.opStack.append(p[1])

def p_logical_op(p):
    '''logical_op : GT
                  | GTE
                  | LT
                  | LTE
                  | NEQ
                  | EQ'''
    p[0] = p[1]
    code.opStack.append(p[1])

def p_sums(p):
    '''sums : MINUS 
            | PLUS '''
    p[0] = p[1]
    code.opStack.append(p[1])
    
def p_multdiv(p):
    '''multdiv : TIMES 
               | DIVIDE '''
    p[0] = p[1]
    code.opStack.append(p[1])

# -- Expresiones --
def p_megaexp(p):
    '''megaexp : superexp
               | megaexp boolean_op superexp'''
    nextOp = code.peek(code.opStack) 
    if (nextOp in ['&', '|']):
        code.buildExp()

def p_superexp(p):
    '''superexp : exp
                | superexp logical_op exp'''
    nextOp = code.peek(code.opStack) 
    if (nextOp in ['<', '<=', '>', '>=', '!=', '==']):
        code.buildExp()

def p_exp(p):
    '''exp : termino
           | exp sums termino'''
    nextOp = code.peek(code.opStack) 
    if (nextOp in ['+', '-']):
        code.buildExp()

def p_termino(p):
    '''termino : factor
               | termino multdiv factor'''
    nextOp = code.peek(code.opStack) 
    if (nextOp in ['*', '/']):
        code.buildExp()

def p_factor(p):
    '''factor : vcte
              | openpar megaexp closepar'''

# agregar fondo falso a opstack
def p_openpar(p): 
    'openpar : OPENPAR'
    code.opStack.append(p[1])

# quitar fondo falso
def p_closepar(p): 
    'closepar : CLOSEPAR'
    code.opStack.pop()

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
