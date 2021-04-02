import ply.lex as lex
import ply.yacc as yacc
import sys,os

###############################################
#TOKENS
###############################################

reserved = {#reserverd tokens
    'else': 'ELSE',
    'int' : 'INT',
    'var' : 'VAR',
    'float': 'FLOAT',
    'bool' :'BOOL',
    'print': 'PRINT',
    'read' : 'READ',
    'and' : 'AND',
    'or': 'OR',
    'not' : 'NOT',
    'end':'END',
    'avergage': 'AVERAGE',
    'void' :'VOID',
    'func' : 'FUNC',
    'char' : 'CHAR',
    'main': 'MAIN',
    'dataset': 'DATASET',
    'cond' : 'CONDITION',
}

tokens = [
         'CTE_I', 'CTE_F', 'CTE_STRING','t_CTE_CHAR','CTE_BOOLEAN', 'ID',
         'TIMES', 'DIVIDE', 'SEMICOLON',
         'OPENP', 'CLOSEP', 'COMA',
         'OPENC', 'CLOSEC', 'COLON',
         'EQUAL', 'GREATERTHAN', 'LESSTHAN',
         'DIFERENT', 'MINUS', 'PLUS',
         ] + list(reserved.values())

t_MINUS = r'\-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_SEMICOLON = r'\;'
t_OPENP = r'\('
t_CLOSEP = r'\)'
t_COMA = r'\,'
t_EQUAL = r'\='
t_OPENC = r'\{'
t_CLOSEC = r'\}'
t_COLON = r'\:'
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_DIFERENT = r'\<>'
#to ignore characteres:
t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_\d]*'
    t.type = reserved.get(t.value, 'ID')
    return t
    
def t_CTE_I(t):
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t
    
def t_CTE_F(t):
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_STRING(t):
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t

def t_CTE_CHAR(t):
    r'(\'[^\']*\')'
    t.value = t.value.strip("'")
    return t

def t_CTE_BOOLEAN(t):
    r'(TRUE|FALSE)'
    if t.value == 'TRUE':
        t.value = True
    else:
        t.value = False
    return t



# el lexer
#Un ejemplo para aplicar las reglas de : Programa Id DOS PUNTOS REGLA END.....
lex.lex()

def p_programa(p):

    p[0] = 'Compiled Program'


def p_empty(p):
    '''
        empty :
    '''
    p[0] = None


def p_error(p):
   print("Syntax error on the Input", p)
   
#analizador lexico

#codigo Prueba para verificar que el analizador sirva
yacc.yacc()

def usaArchivo():
    try:
        archivo = 'prueba incorrecta.txt'
        arch = open(archivo, 'r')
        print("Filename used : " + archivo)
        info = arch.read()
        arch.close()
        lexer.input(info)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
        if (yacc.parse(info, tracking=True) == 'Compiled Program'):
            print("No syntax errors")
        else:
            print("Syntax Error")
    except EOFError:
        print(EF)

usaArchivo()
