import ply.lex as lex
import exceptions

# === LEXER ===
tokens = [
    'SEMICOLON', 'COMMA',
    'PLUS', 'MINUS','TIMES','DIVIDE', 'ASSIGN',
    'GTE', 'LTE', 'NEQ', 'EQ', 'GT', 'LT', 'AND', 'OR',
    'LCURLYB', 'RCURLYB', 'OPENPAR', 'CLOSEPAR', 'OPENBRAC', 'CLOSEBRAC',
    'ID', 'CTEI', 'CTEF', 'CTES', 'CTEC',
    'DETERM', 'TRANSPOSE', 'INVERSE',
    'COMMENT'
]

# Reserved 
reserved = {
    'programa': 'PROGRAMA',
    'principal': 'PRINCIPAL',
    'var' : 'VAR',
    'funcion': 'FUNCION',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'bool': 'BOOL',
    'void': 'VOID',
    'si': 'SI',
    'entonces': 'ENTONCES',
    'sino': 'SINO',
    'mientras': 'MIENTRAS',
    'haz': 'HAZ',
    'desde': 'DESDE',
    'hasta': 'HASTA',
    'hacer': 'HACER',
    'quackin': 'QUACKIN',
    'quackout': 'QUACKOUT',
    'retorna': 'RETORNA',
    'true': 'TRUE',
    'false': 'FALSE'
}

tokens += reserved.values()

# Tokens
t_AND       = r'&'
t_OR     = r'\|'
t_GT        = r'>'
t_GTE       = r'>='
t_LT        = r'<'
t_LTE       = r'<='
t_NEQ       = r'!='
t_EQ        = r'=='
t_LCURLYB   = r'{'
t_RCURLYB   = r'}'
t_OPENPAR   = r'\('
t_CLOSEPAR  = r'\)'
t_OPENBRAC  = r'\['
t_CLOSEBRAC = r'\]'
t_SEMICOLON = r';'
t_COMMA     = r','
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r'='
t_DETERM    = r'\$'
t_TRANSPOSE = r'!'
t_INVERSE   = r'\^'


def t_CTEF(t):
    r'\d*\.\d+'
    return t

def t_CTEI(t):
    r'\d+'
    return t
    
def t_CTEC(t):
    r"'.'"
    return t
    
def t_CTES(t):
    r'"([^"\n]|(\\"))*"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved.get(t.value, 'ID')
    return t

def t_COMMENT(t):
    r'\%%.*'
    pass

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    exceptions.fatalError("Illegal character '%s' in line '%d'" % (lexer.token(), t.lexer.lineno))

# Build the lexer
lexer = lex.lex()
