# PARA HACER PRUEBAS DE ALGUNAS DE REGLAS Y CHECAR QUE ESTEN FUNCIONANDO
# Parsing rules
import patitoLexer
import codeGenerator as cd
import ply.yacc as yacc

tokens = patitoLexer.tokens
code = cd.CodeGenerator()

# -- Expresiones
def p_exp(p):
    '''exp : termino exp2'''

def p_exp2(p):
    '''exp2 : sums exp
            | empty'''
    if(p[1] is not None): 
        code.generate()
    # sale y resuelve sumas/restas pendientes osea esta bien
    #como se arregla xddd

def p_termino(p):
    '''termino : factor termino2'''

def p_termino2(p):
    '''termino2 : multdiv termino
                | empty'''
    if(p[1] is not None): 
        code.generate()
        #pasé esto a codeGenerator??
        #popDer = code.idStack.pop()
        #popIzq = code.idStack.pop()
        #popOper = code.opStack.pop()
        #print("popDer", popDer)
        #print("popIzq", popIzq)
        #print("popOper", popOper) #checar si es * o / y resolver, sino no, iwal arriba supongo
        #print("t"+str(code.cont))
        #code.generate(popOper, popIzq, popDer, "t"+str(code.cont))
        #code.cont += 1

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
    print("factor", p[1])

def p_sums(p):
    '''sums : MINUS 
            | PLUS '''
    p[0] = p[1]
    code.opStack.append(p[1])
    print("sums", p[1])

def p_multdiv(p):
    '''multdiv : TIMES 
               | DIVIDE '''
    code.opStack.append(p[1])
    p[0] = p[1]
    print("mult", p[1])

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
    parser.parse(s, debug=1)
