# === PARSER ===
# Parsing rules
import patitoLexer
import codeGenerator as cg
import ply.yacc as yacc
import sys

tokens = patitoLexer.tokens
code = cg.CodeGenerator()

EMPTY = '$'

precedence = (
    ('left', 'COMMA'),
)

def p_program_declaration(p):
    'program_declaration : PROGRAMA ID SEMICOLON declare_vars declare_func_rec declare_main OPENPAR CLOSEPAR bloque_funcion'
    global programId
    programId = p[2]
    code.endFunc()


#def p_principal(p):
    #code.startMain()

def p_declare_main(p):
    '''declare_main : PRINCIPAL'''
    code.registerFunc('principal', 'void')

def p_declare_vars(p):
    '''declare_vars : VAR vars
                    | empty'''

def p_vars(p):
    '''vars : var_id dimensions more_vars SEMICOLON vars
            | empty'''
    print("End of var declaration")

def p_var_id(p):
    '''var_id : tipo ID'''
    #Falta identificar entre globales y las que pertecen a una función
    code.registerVariable(p[2], p[1])

def p_more_vars(p):
    '''more_vars : more_var_id dimensions more_vars
                 | empty'''

def p_more_var_id(p):
    '''more_var_id : COMMA ID'''
    if(p[2] != None and p[2] != EMPTY):
        code.registerVariable(p[2], None)


def p_dimensions(p):
    '''dimensions : OPENBRAC CTEI CLOSEBRAC 
                  | OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRAC
                  | empty'''

def p_declare_func_rec(p):
    '''declare_func_rec : declare_func_rec declare_func
                        | empty'''

def p_declare_func(p):
    '''declare_func : FUNCION func_id OPENPAR declare_func_params CLOSEPAR bloque_funcion'''
    code.endFunc()

def p_func_id(p):
    '''func_id : tipo ID
               | VOID ID'''
    code.registerFunc(id=p[2], tipo=p[1])

def p_declare_func_params(p):
    '''declare_func_params : get_func_params more_params
                           | empty'''

def p_get_func_params(p):
    '''get_func_params : tipo ID'''
    code.registerFuncParams(id=p[2], tipo=p[1])

def p_more_params(p):
    '''more_params : more_var_id more_params
                   | empty'''

def p_more_params_id(p):
    '''more_var_id : COMMA tipo ID'''
    code.registerFuncParams(id=p[3], tipo=p[2])

def p_tipo(p):
    '''tipo : INT 
            | FLOAT
            | CHAR
            | BOOL'''
    p[0] = p[1]

# Ahora las variables de cada funcion se declaran al principio del bloque
def p_bloque_funcion(p):
    'bloque_funcion : LCURLYB declare_vars estatutos_rec RCURLYB'

#bloque sin variables para if, for, while etc.
def p_bloque(p):
    'bloque : LCURLYB estatutos_rec RCURLYB'

def p_estatutos_rec(p):
    '''estatutos_rec : estatuto estatutos_rec
                     | empty''' 

def p_estatuto(p):
    '''estatuto : asignacion 
                | condicion 
                | func_void
                | retorno
                | escribe
                | lee 
                | desde
                | mientras_estatuto'''

# -- Asignacion --
def p_asignacion(p):
    "asignacion : id ASSIGN megaexp SEMICOLON"

# -- Condicion --
def p_condicion(p):
    "condicion : SI OPENPAR megaexp CLOSEPAR entonces bloque_entonces"

def p_entonces(p):
    'entonces : ENTONCES'
    code.ifStart()

def p_condicion_entonces(p):
    "bloque_entonces : bloque bloque_sino"

def p_bloque_sino(p):
    '''bloque_sino : sino bloque 
                   | empty'''
    code.ifEnd()

def p_condicion_sino(p):
    'sino : SINO'
    code.ifElse()

# -- Funcion void --
def p_func_void(p):
    'func_void : func_call_id OPENPAR func_call_params CLOSEPAR SEMICOLON'
    code.funcCallEnd()

def p_func_call_id(p):
    'func_call_id : ID'
    code.funcCallStart(p[1])

def p_func_call_params(p):
    '''func_call_params : func_call_params COMMA func_call_params
                        | empty'''

def p_func_call_add_params(p):
    'func_call_params : megaexp'
    code.funcCallParam()

# -- Escribir --
def p_escribe(p):
    "escribe : QUACKOUT OPENPAR print_options CLOSEPAR SEMICOLON"

def p_print_options(p):
    '''print_options : CTES more_print
                     | megaexp more_print'''

def p_more_print(p):
    '''more_print : COMMA CTES
                  | COMMA megaexp
                  | empty'''

# -- Leer --
def p_lee(p):
    '''lee : QUACKIN OPENPAR ID read_more CLOSEPAR SEMICOLON'''

def p_read_more(p):
    '''read_more : COMMA ID read_more
                 | empty'''

# -- Retorno --
def p_retorno(p):
    'retorno : RETORNO OPENPAR megaexp CLOSEPAR SEMICOLON'

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

# -- Mientras --
def p_mientras_estatuto(p):
    '''mientras_estatuto : mientras OPENPAR megaexp CLOSEPAR haz bloque'''
    # goto migajita y llenar gotof
    code.whileEnd()

def p_mientras(p):
    'mientras : MIENTRAS'
    # migajita 
    code.whileStart()

def p_mientras_haz(p):
    'haz : HAZ'
    #gotoFalso a no sé dónde
    code.whileDo()


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

# ID o acceso a arreglo
def p_id(p):
    '''id : ID
          | ID OPENBRAC exp CLOSEBRAC
          | ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRAC'''
    p[0] = p[1]

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


# -- Error y empty --
def p_empty(p):
    'empty :'
    p[0] = EMPTY

def p_error(p):
    print("error")

# -- Crea el parser y loop para leer --
parser = yacc.yacc()

while True:
    try:
        s = input('test > ')
        if s == '$':
            sys.exit()
    except EOFError:
        break
    parser.parse(s, debug=0)
