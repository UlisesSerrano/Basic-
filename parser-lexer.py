import sys
import ply.lex as lex
import ply.yacc as yacc

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
    'CTE_I', 'CTE_F', 'CTE_STRING', 'CTE_CHAR', 'ID',
    'MULT', 'DIV', 'SEMICOLON',
    'L_P', 'R_P', 'COMA',
    'L_B', 'R_B',
    'L_SB', 'R_SB',
    'EQUAL', 'GREATERTHAN', 'LESSTHAN',
    'GREATERTHANEQ', 'LESSTHANEQ', 'EQ',
    'DIFERENT', 'AND', 'OR',
    'MINUS', 'PLUS', 'MOD'
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
t_R_SB = r'\]'
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
    r'\d*\.\d+'
    t.value = float(t.value)
    return t


def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTE_STRING(t):
    r'"([^"\n]|(\\"))*"$'
    print ("String: '%s'" % t.value)
    return t


def t_CTE_CHAR(t):
    r'(\'[^\']*\')'
    t.value = t.value.strip("'")
    return t


# el lexer
# Un ejemplo para aplicar las reglas de : Programa Id DOS PUNTOS REGLA END.....
lexer = lex.lex()


def p_program(p):
    '''program : PROGRAM ID SEMICOLON g_var funcs main'''


def p_main(p):
    '''main : MAIN L_P params R_P var_declaration L_B statements R_B'''


def p_type(p):
    '''type : INT 
            | FLOAT 
            | CHAR'''


def p_g_var(p):
    '''g_var : var_declaration
            | empty'''


def p_funcs(p):
    '''funcs : function funcs
            | empty'''


def p_var_declaration(p):
    '''var_declaration : VAR var1
                        | empty'''


def p_var1(p):
    '''var1 : var_type dec_id var2 SEMICOLON var4'''



def p_var2(p):
    '''var2 : COMA dec_id var3
            | empty'''


def p_var3(p):
    '''var3 : var2'''


def p_var4(p):
    '''var4 : var1
            | empty'''

def p_dec_id(p):
    '''dec_id : ID dec_id1'''


def p_dec_id1(p):
    '''dec_id1 : L_SB CTE_I R_SB dec_id2
            | empty'''


def p_dec_id2(p):
    '''dec_id2 : L_SB CTE_I R_SB
        | empty'''

def p_id(p):
    '''id : ID id1'''


def p_id1(p):
    '''id1 : L_SB expression R_SB id2
            | empty'''


def p_id2(p):
    '''id2 : L_SB expression R_SB
        | empty'''


def p_var_type(p):
    '''var_type : type'''


def p_function(p):
    '''function : FUNC func_type ID L_P params R_P var_declaration L_B statements R_B'''

def p_func_type(p):
    '''func_type : VOID
                | type'''


def p_params(p):
    '''params : var_type id params1
            | empty'''


def p_params1(p):
    '''params1 : COMA params
                | empty'''


def p_statements(p):
    '''statements : statement statements
                | empty'''


def p_statement(p):
    '''statement : assignation
                | call_func
                | return_func
                | read
                | write
                | decision_statement
                | repetition_statement
                | expression'''


def p_assignation(p):
    '''assignation : id EQUAL expression SEMICOLON'''


def p_args(p):
    '''args : args1
            | empty'''


def p_args1(p):
    'args1 : expression args2'


def p_args2(p):
    '''args2 : COMA args1
            | empty'''


def p_call_func(p):
    '''call_func :  ID L_P args R_P SEMICOLON'''


def p_return_func(p):
    '''return_func : RETURN L_P expression R_P SEMICOLON'''


def p_read(p):
    '''read : READ L_P read_args R_P SEMICOLON'''


def p_read_args(p):
    '''read_args : expression read_args1'''


def p_read_args1(p):
    '''read_args1 : COMA expression read_args1
                | empty'''


def p_write(p):
    '''write : PRINT L_P write_args R_P SEMICOLON'''


def p_write_args(p):
    '''write_args : write_args2 write_args1'''


def p_write_args1(p):
    '''write_args1 : COMA write_args2 write_args1
                    | empty'''


def p_write_args2(p):
    '''write_args2 : expression
                | CTE_STRING'''


def p_decision_statement(p):
    '''decision_statement : IF L_P expression R_P L_B statements R_B decision_statement1'''


def p_decision_statement1(p):
    '''decision_statement1 : ELSE L_B statements R_B
                            | empty'''


def p_repetition_statement(p):
    '''repetition_statement : while_statement
                            | for_statement'''


def p_for_statement(p):
    '''for_statement : FOR id EQUAL expression TO expression do_statement'''


def p_while_statement(p):
    '''while_statement : WHILE L_P expression R_P do_statement'''


def p_do_statement(p):
    '''do_statement :  DO L_B statements R_B'''


def p_expression(p):
    '''expression : texp op1'''


def p_texp(p):
    '''texp : gexp op2'''


def p_gexp(p):
    '''gexp : mexp op3aux'''


def p_mexp(p):
    '''mexp : term op4aux'''


def p_term(p):
    '''term : fact op5aux'''


def p_fact(p):
    '''fact : ID fact1
            | L_P expression R_P
            | cte'''


def p_fact1(p):
    '''fact1 : L_P args R_P
            | id1'''


def p_cte(p):
    '''cte : CTE_I
            | CTE_F
            | CTE_CHAR'''


def p_op1(p):
    '''op1 : OR expression
            | empty'''


def p_op2(p):
    '''op2 : AND texp
            | empty'''


def p_op3(p):
    '''op3 : LESSTHAN
            | LESSTHANEQ 
            | GREATERTHAN
            | GREATERTHANEQ
            | EQ
            | DIFERENT'''


def p_op3aux(p):
    '''op3aux : op3 mexp
            | empty'''


def p_op4(p):
    '''op4 : PLUS
            | MINUS'''


def p_op4aux(p):
    '''op4aux : op4 mexp
            | empty'''


def p_op5(p):
    '''op5 : MULT
        | DIV
        | MOD'''


def p_op5aux(p):
    '''op5aux : op5 term
            | empty'''


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
        if (yacc.parse(info, tracking=True) == 'Compiled Program'):
            print("No syntax errors")
        else:
            print("Syntax Error")
    except EOFError:
        print(EOFError)


usaArchivo()
