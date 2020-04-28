# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

# -- Expresiones

def p_megaexp(p):
    '''megaexp : superexp megaexp2'''

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
    if (p[1] is not None):
        nextOp = code.peek(code.opStack) 
        if (nextOp == '+' or nextOp == '-'):
            code.generate()


def p_termino(p):
    '''termino : factor termino2'''

def p_termino2(p):
    '''termino2 : multdiv termino
                | empty'''
    if (p[1] is not None):
        nextOp = code.peek(code.opStack) 
        if (nextOp == '*' or nextOp == '/'):
            code.generate()

def p_factor(p):
    '''factor : vcte
              | OPENPAR exp CLOSEPAR'''
    p[0] = p[1]

def p_vcte(p):
    '''vcte : ID
            | CTEI
            | CTEF
            | CTEC
            | TRUE
            | FALSE'''
    p[0] = p[1]
    code.idStack.append(p[1])

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
    p[0] = p[1]
    code.opStack.append(p[1])
    
def p_multdiv(p):
    '''multdiv : TIMES 
               | DIVIDE '''
    p[0] = p[1]
    code.opStack.append(p[1])

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
