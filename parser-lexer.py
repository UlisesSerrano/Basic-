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
    'CTE_I', 'CTE_F', 'CTE_STRING', 'CTE_CHAR', 'CTE_BOOLEAN', 'ID',
    'MULT', 'DIV', 'SEMICOLON',
    'L_P', 'R_P', 'COMA',
    'L_B', 'R_B',
    'L_SB', 'R_SB',
    'EQUAL', 'GREATERTHAN', 'LESSTHAN',
    'GREATERTHANEQ', 'LESSTHANEQ', 'EQ',
    'DIFERENT', 'AND', 'OR', 'NOT',
    'MINUS', 'PLUS', 'MOD',
] + list(reserved.values())

t_MINUS = r'\-'
t_PLUS = r'\+'
t_MULT = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_SEMICOLON = r'\;'
t_L_P = r'\('
t_R_P = r'\)'
t_COMA = r'\,'
t_L_B = r'\{'
t_R_B = r'\}'
t_L_SB = r'\['
t_R_SB = r'\['
t_AND = r'\&\&'
t_OR = r'\|\|'
t_EQ = r'\=\='
t_GREATERTHANEQ = r'\>\='
t_LESSTHANEQ = r'\<\='
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_DIFERENT = r'\!\='
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
    '''g_var : var_declaration 
            | empty'''
    p[0] = p[1]


def p_funcs(p):
    '''funcs : function funcs
            | empty'''
    p[0] = p[1]


def p_var_declaration(p):
    '''var_declaration : VAR var1
                        | empty'''
    p[0] = p[1]


def p_var1(p):
    'var1 : var_type id var2 SEMICOLON var4'
    p[0] = p[1]


def p_var2(p):
    '''var2 : COMA id var3
            | empty'''
    p[0] = p[1]


def p_var3(p):
    '''var3 : var2
            | empty'''
    p[0] = p[1]


def p_var4(p):
    '''var4 : var1
        | empty'''
    p[0] = p[1]


def p_id(p):
    'id : ID id1'
    p[0] = p[1]


def p_id1(p):
    '''id1 : L_SB expression R_SB id2
        | empty'''
    p[0] = p[1]


def p_id2(p):
    '''id2 : L_SB expression R_SB
        | empty'''
    p[0] = p[1]


def p_type(p):
    '''type : INT 
            | FLOAT 
            | CHAR'''
    p[0] = p[1]


def p_var_type(p):
    'var_type : type'
    p[0] = p[1]


def p_function(p):
    'function : func_type FUNC ID L_P params R_P var_declaration L_B statements R_B'
    p[0] = p[1]


def p_func_type(p):
    '''func_type : VOID
                | type'''
    p[0] = p[1]


def p_params(p):
    '''params : var_type id params1
            | empty'''
    p[0] = p[1]


def p_params1(p):
    '''params1 : COMA params
                | empty'''
    p[0] = p[1]


def p_statements(p):
    '''statements : statement statements
                | empty'''
    p[0] = p[1]


def p_statement(p):
    '''statement : assignation
                | call_func
                | return_func
                | read
                | write
                | decision_statement
                | repetition_statement
                | expression'''
    p[0] = p[1]


def p_assignation(p):
    'assignation : id EQUAL expression SEMICOLON'
    p[0] = p[1]


def p_args(p):
    '''args : args1
            | empty'''
    p[0] = p[1]


def p_args1(p):
    'args1 : expression args2'
    p[0] = p[1]


def p_args2(p):
    '''args2 : COMA args1
            | empty'''
    p[0] = p[1]


def p_call_func(p):
    'call_func :  ID L_P args R_P SEMICOLON'
    p[0] = p[1]


def p_return_func(p):
    'return_func : RETURN L_P expression R_P SEMICOLON'
    p[0] = p[1]


def p_read(p):
    'read : READ L_P read_args R_P SEMICOLON'
    p[0] = p[1]


def p_read_args(p):
    'read_args : expression read_args1'
    p[0] = p[1]


def p_read_args1(p):
    '''read_args1 : COMA expression read_args1
                | empty'''
    p[0] = p[1]


def p_write(p):
    'write : PRINT L_P write_args R_P SEMICOLON'
    p[0] = p[1]


def p_write_args(p):
    'write_args : write_args2 write_args1'
    p[0] = p[1]


def p_write_args1(p):
    '''write_args1 : COMA write_args2 write_args1
                    | empty'''
    p[0] = p[1]


def p_write_args2(p):
    '''write_args2 : expression
                | CTE_STRING'''
    p[0] = p[1]


def p_decision_statement(p):
    'decision_statement : IF L_P expression R_P L_B statements R_B decision_statement1'
    p[0] = p[1]


def p_decision_statement1(p):
    '''decision_statement1 : ELSE L_B statements R_B
                            | empty'''
    p[0] = p[1]


def p_repetition_statement(p):
    '''repetition_statement : while_statement
                            | for_statement'''
    p[0] = p[1]


def p_for_statement(p):
    'for_statement : FOR id EQUAL expression TO expression do_statement'
    p[0] = p[1]


def p_while_statement(p):
    'while_statement : WHILE L_P expression R_P do_statement'
    p[0] = p[1]


def p_do_statement(p):
    'do_statement :  DO L_B statements R_B'
    p[0] = p[1]


def p_expression(p):
    'expression : texp op1'
    p[0] = p[1]


def p_texp(p):
    'texp : gexp op2'
    p[0] = p[1]


def p_gexp(p):
    'gexp : nexp op3aux'
    p[0] = p[1]


def p_nexp(p):
    'nexp : term op4aux'
    p[0] = p[1]


def p_term(p):
    'term : fact op5aux'
    p[0] = p[1]


def p_fact(p):
    '''fact : ID fact1
            | L_P expression R_P
            | cte'''
    p[0] = p[1]


def p_fact1(p):
    '''fact1 : L_P args R_P
            | id1
            | empty'''

def p_cte(p):
    '''cte : CTE_I
            | CTE_F
            | CTE_CHAR'''


def p_op1(p):
    '''op1 : OR expression
            | empty'''
    p[0] = p[1]


def p_op2(p):
    '''op2 : AND texp
            | empty'''
    p[0] = p[1]


def p_op3(p):
    '''op3 : LESSTHAN
            | LESSTHANEQ 
            | GREATERTHAN
            | GREATERTHANEQ
            | EQ
            | DIFERENT'''
    p[0] = p[1]

def p_op3aux(p):
    '''op3aux : op3 gexp
            | empty'''
    p[0] = p[1]


def p_op4(p):
    '''op4 : PLUS
            | MINUS'''
    p[0] = p[1]


def p_op4aux(p):
    '''op4aux : op4 nexp
            | empty'''
    p[0] = p[1]


def p_op5(p):
    '''op5 : MULT
        | DIV
        | MOD'''
    p[0] = p[1]


def p_op5aux(p):
    '''op5aux : op5 term
            | empty'''
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
        archivo = 'test.txt'
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
