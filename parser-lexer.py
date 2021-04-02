import ply.lex as lex
import ply.yacc as yacc
import sys
import os

###############################################
# TOKENS
###############################################

reserved = {  # reserverd tokens
    'program': 'PROGRAM',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'char': 'CHAR',
    'print': 'PRINT',
    'read': 'READ',
    'void': 'VOID',
    'func': 'FUNC',
    'main': 'MAIN',
    'return': 'RETURN',
    'do': 'DO',
    'while': 'WHILE',
    'for': 'FOR',
    'to': 'TO'
}

tokens = [
    'CTE_I', 'CTE_F', 'CTE_STRING', 't_CTE_CHAR', 'CTE_BOOLEAN', 'ID',
    'TIMES', 'DIVIDE', 'SEMICOLON',
    'L_P', 'R_P', 'COMA',
    'L_B', 'R_B', 'COLON',
    'OPENB', 'R_SB',
    'EQUAL', 'GREATERTHAN', 'LESSTHAN',
    'GREATERTHANEQ', 'LESSTHANEQ', 'EQ'
    'DIFERENT', 'AND', 'OR', 'NOT'
    'MINUS', 'PLUS', 'MOD',
] + list(reserved.values())

t_MINUS = r'\-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MOD = r'\%'
t_SEMICOLON = r'\;'
t_L_P = r'\('
t_R_P = r'\)'
t_COMA = r'\,'
t_L_B = r'\{'
t_R_B = r'\}'
t_L_SB = r'\['
t_R_SB = r'\['
t_COLON = r'\:'
t_AND = r'\&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_EQ = r'\=='
t_GREATERTHANEQ = r'\>='
t_LESSTHANEQ = r'\<='
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_DIFERENT = r'\!='
t_EQUAL = r'\='
# para ignorar caracteres:
t_ignore = ' \t\r\n'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_\d]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_CTE_F(t):
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t


def t_CTE_I(t):
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
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
# Un ejemplo para aplicar las reglas de : Programa Id DOS PUNTOS REGLA END.....
lexer = lex.lex()


def p_program(p):
    'program : PROGRAM ID SEMICOLON g_var funcs main'
    p[0] = p[1]


def p_main(p):
    'main : MAIN L_P params R_P var_declaration L_B statements R_B'
    p[0] = p[1]


def p_g_var(p):
    'g_var : var_declaration | empty'
    p[0] = p[1]


def p_funcs(p):
    'funcs : function funcs | empty'
    p[0] = p[1]


def p_var_declaration(p):
    'var_declaration : VAR var1 | empty'
    p[0] = p[1]


def p_var1(p):
    'var1 : var_type id var2 SEMICOLON var4'
    p[0] = p[1]


def p_var2(p):
    'var2 : COMA id var3 | empty'
    p[0] = p[1]


def p_var3(p):
    'var3 : var2 | empty'
    p[0] = p[1]


def p_var4(p):
    'var4 : var1 | empty'
    p[0] = p[1]


def p_id(p):
    'id : ID id1'
    p[0] = p[1]


def p_empty(p):
    '''
        empty :
    '''
    p[0] = None


def p_error(p):
    print("Syntax error on the Input", p)

# analizador lexico


# codigo Prueba para verificar que el analizador sirva
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
        print('EOF')


usaArchivo()
