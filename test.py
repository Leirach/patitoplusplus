# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

#stacks 
opStack = []
idStack = []

# -- Expresiones
def p_megaexp(p):
    '''megaexp : superexp megaexp2'''
    print(p[0], p[1])

def p_megaexp2(p):
    '''megaexp2 : blooean_op megaexp
                | empty'''

def p_superexp(p):
    '''superexp : exp superexp2'''

def p_superexp2(p):
    '''superexp2 : logical_op superexp
                 | empty'''

def p_exp(p):
    '''exp : termino exp2'''

def p_exp2(p):
    '''exp2 : sums exp
            | empty'''

def p_termino(p):
    '''termino : factor termino2'''

def p_termino2(p):
    '''termino2 : multdiv factor
                | empty'''

def p_factor(p):
    '''factor : vcte
              | OPENPAR megaexp CLOSEPAR'''
            
def p_vcte(p):
    '''vcte : ID
            | CTEI
            | CTEF
            | CTEC
            | TRUE
            | FALSE'''

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
    parser.parse(s, debug=1) #puse debug D:
