# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc
import sys

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

EMPTY = '$'

precedence = (
    ('left', 'COMMA'),
)

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

def p_factor_unary_op(p):
    '''factor : unary_ops vcte
              | unary_ops openpar megaexp closepar'''
    code.buildUnaryExp()

# agregar fondo falso a opstack
def p_openpar(p):
    'openpar : OPENPAR'
    code.opStack.append(p[1])

# quitar fondo falso
def p_closepar(p):
    'closepar : CLOSEPAR'
    code.opStack.pop()

def p_vcte_ID(p):
    'vcte : id'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append(code.getVarType(p[1]))

def p_vcte_CTEI(p):
    'vcte : CTEI'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('int')

def p_vcte_CTEF(p):
    'vcte : CTEF'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('float')

def p_vcte_CTEB(p):
    '''vcte : TRUE
            | FALSE'''
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('bool')

def p_vcte_CTEC(p):
    'vcte : CTEC'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('char')

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

def p_unary_ops(p):
    '''unary_ops : MINUS
                 | PLUS
                 | DETERM
                 | TRANSPOSE
                 | INVERSE'''
    code.opStack.append(p[1])

def p_id(p):
    '''id : ID
          | ID OPENBRAC exp CLOSEBRAC
          | ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRAC'''
    p[0] = p[1]

# -- Error y empty --
def p_empty(p):
    'empty :'
    p[0] = EMPTY

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
