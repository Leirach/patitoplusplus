# === PARSER ===
# Parsing rules
import patitoLexer
import codeGenerator as cg
import ply.yacc as yacc
import exceptions
import sys

tokens = patitoLexer.tokens

EMPTY = '$'

precedence = (
    ('left', 'COMMA'),
)

def p_program_declaration(p):
    'program_declaration : PROGRAMA ID SEMICOLON declare_vars declare_func_rec declare_main OPENPAR CLOSEPAR bloque_funcion'
    code.endFunc()

def p_declare_main(p):
    '''declare_main : PRINCIPAL'''
    code.registerFunc('principal', 'void')

def p_declare_vars(p):
    '''declare_vars : VAR vars
                    | empty'''

def p_vars(p):
    '''vars : first_var more_vars SEMICOLON vars
            | empty'''

def p_first_var(p):
    '''first_var : tipo ID dimensions'''
    # p[3][0] dimension1
    # p[3][1] dimension2
    code.registerVariable(p[2], p[1], p[3][0], p[3][1])

def p_more_vars(p):
    '''more_vars : more_var_id more_vars
                 | empty'''

def p_more_var_id(p):
    'more_var_id : COMMA ID dimensions'
    code.registerVariable(p[2], None, p[3][0], p[3][1])

def p_dimensions_empty(p):
    'dimensions : empty'
    p[0] = [None, None]

def p_dimensions_one(p):
    'dimensions : OPENBRAC CTEI CLOSEBRAC'
    p[0] = [int(p[2]), None]

def p_dimensions_two(p):
    'dimensions : OPENBRAC CTEI CLOSEBRAC OPENBRAC CTEI CLOSEBRAC'
    p[0] = [int(p[2]), int(p[5])]


def p_declare_func_rec(p):
    '''declare_func_rec : declare_func_rec declare_func
                        | empty'''

def p_declare_func(p):
    '''declare_func : FUNCION func_id OPENPAR declare_func_params CLOSEPAR bloque_funcion'''
    code.endFunc()

def p_func_id(p):
    '''func_id : tipo ID
               | VOID ID'''
    code.registerFunc(functionName=p[2], functionType=p[1])

def p_declare_func_params(p):
    '''declare_func_params : get_func_params more_params
                           | empty'''

def p_get_func_params(p):
    '''get_func_params : tipo ID'''
    code.registerFuncParams(paramId=p[2], paramType=p[1])

def p_more_params(p):
    '''more_params : more_var_id more_params
                   | empty'''

def p_more_params_id(p):
    '''more_var_id : COMMA tipo ID'''
    code.registerFuncParams(paramId=p[3], paramType=p[2])

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
    '''estatuto : asignacion SEMICOLON
                | condicion 
                | func_call SEMICOLON
                | retorna
                | escribe
                | lee 
                | desde
                | mientras_estatuto'''

# -- Asignacion --
def p_asignacion(p):
    "asignacion : id ASSIGN megaexp"
    code.buildAssign()

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
def p_func_call(p):
    'func_call : func_call_id openpar func_call_params closepar'
    p[0] = p[1]         # para retorno en una expresion
    code.funcCallEnd()

def p_func_call_id(p):
    'func_call_id : ID'
    p[0] = p[1]
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

def p_print_multi(p):
    '''print_options : print_options COMMA printable
                     | printable'''
    code.ioQuad('PRINT')

def p_printable_exp(p):
    'printable : megaexp'
def p_printable(p):
    'printable : CTES'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('char')
    code.memStack.append('const')

# -- Leer --
def p_lee(p):
    '''lee : QUACKIN OPENPAR read_options CLOSEPAR SEMICOLON'''

def p_read_options(p):
    '''read_options : read_options COMMA id
                    | id'''
    code.ioQuad('READ')

# -- Retorna --
def p_retorna(p):
    'retorna : RETORNA OPENPAR megaexp CLOSEPAR SEMICOLON'
    code.retorna()

# -- Desde --
def p_desde(p):
    '''desde : DESDE id ASSIGN exp hasta exp hacer bloque'''
    code.forEnd()

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

# ID o acceso a arreglo
def p_id(p):
    'id : ID'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append(code.getVarType(p[1]))
    code.memStack.append('var')

# falta poner breaks en operaciones 
# o sea, openbrac, en vez de OPENBRAC, como regla que haga push a opstack('[')
# y closebrac que haga pop
def p_id_dimensions_one(p):
    'id : ID OPENBRAC exp CLOSEBRAC'
    p[0] = p[1]
    code.accessArray(p[1], 'dim1')

def p_id_dimensions_two(p):
    'id : ID OPENBRAC exp CLOSEBRAC OPENBRAC exp CLOSEBRAC'
    p[0] = p[1]
    code.accessArray(p[1], 'dim2')

def p_vcte_func_call(p):
    'vcte : func_call'
    code.funcCallReturn(p[1])

def p_vcte_CTEI(p):
    'vcte : CTEI'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('int')
    code.memStack.append('const')

def p_vcte_CTEF(p):
    'vcte : CTEF'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('float')
    code.memStack.append('const')

def p_vcte_CTEB(p):
    '''vcte : TRUE
            | FALSE'''
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('bool')
    code.memStack.append('const')

def p_vcte_CTEC(p):
    'vcte : CTEC'
    p[0] = p[1]
    code.idStack.append(p[1])
    code.tpStack.append('char')
    code.memStack.append('const')

# arreglos como constantes no se si esto tiene que ir D:
# def p_array(p):
#     'array : OPENBRAC arr_elem CLOSEBRAC'

# def p_arr_elem(p):
#     '''arr_elem : arr_elem COMMA vcte
#                 |
#                 | empty'''

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
    print("Syntax error en %s" %p.value)

# -- Crea el parser y loop para leer --
parser = yacc.yacc()

try:
    filename = sys.argv[1]
    if filename == 'debug':
        while True:
            try:
                s = input('test > ')
                if s == '$':
                    sys.exit()
            except EOFError:
                break
            parser.parse(s, debug=0)
except IndexError:
    print('Uso: python patitoParser.py <patito.p>')
    sys.exit()

try:
    f = open(filename, "r")
except FileNotFoundError:
    print("No se encontró el archivo %s" % (filename))
    sys.exit()

source = f.read()
filename = filename.split('.')[0]
code = cg.CodeGenerator(filename)
parser.parse(source, debug=0)
code.saveObj()
