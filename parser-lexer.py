import sys
import ply.lex as lex
import ply.yacc as yacc
from stack import Stack
from semantic_cube import semantic_cube

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
    print("String: '%s'" % t.value)
    return t


def t_CTE_CHAR(t):
    r'(\'[^\']*\')'
    t.value = t.value.strip("'")
    return t


# el lexer
# Un ejemplo para aplicar las reglas de : Programa Id DOS PUNTOS REGLA END.....
lexer = lex.lex()

current_type = ''
current_func = ''
current_id = ''

global_var_table = {}
local_var_table = {}
constant_var_table = {}
dir_func = {}
context = 'global'

param_types = []
variable_counter = {'int': 0, 'float': 0, 'char': 0}

types_stack = Stack()
operators_stack = Stack()
elements_stack = Stack()
jumps_stack = Stack()

quadruples = []
quad_counter = 0

# Variable counter
counter = {
    "global": {
        "int": 0,
        "float": 0,
        "char": 0
    },
    "local": {
        "int": 0,
        "float": 0,
        "char": 0
    },
    "temp": {
        "int": 0,
        "float": 0,
        "char": 0
    },
    "constant": {
        "int": 0,
        "float": 0,
        "char": 0
    }
}

# Base address
address = {
    "global": {
        "int": 1000,
        "float": 4000,
        "char": 7000
    },
    "local": {
        "int": 10000,
        "float": 13000,
        "char": 16000
    },
    "temp": {
        "int": 19000,
        "float": 21000,
        "char": 24000
    },
    "constant": {
        "int": 27000,
        "float": 30000,
        "char": 33000
    }
}


def generate_quadruple():
    global quadruples, quad_counter, address, counter, elements_stack, types_stack, operators_stack
    right_op = elements_stack.pop()
    right_type = types_stack.pop()
    left_op = elements_stack.pop()
    left_type = types_stack.pop()
    op = operators_stack.pop()
    result_type = semantic_cube[left_type][op][right_type]

    if result_type != None:
        result = 0
        result = address['temp'][result_type] + counter['temp'][result_type]
        counter['temp'][result_type] += 1

        print("op:", op)
        print("left:", left_op)
        print("right:", right_op)
        print("result:", result)
        quadruples.append((op, left_op, right_op, result))
        quad_counter += 1

        elements_stack.push(result)
        types_stack.push(result_type)

    else:
        print("ERROR: Type mismatch")


def p_program(p):
    '''program : PROGRAM ID SEMICOLON g_var funcs main'''
    global dir_func, quadruples
    print(dir_func)
    print(quadruples)


def p_main(p):
    '''main : MAIN L_P params R_P var_declaration L_B statements R_B'''
    global local_var_table, param_types, variable_counter
    current_func = 'main'
    if current_func not in dir_func:
        dir_func[current_func] = (
            current_func, 'void', param_types, variable_counter)
    else:
        print('ERROR: Función declarada', current_func)

    print(local_var_table)
    local_var_table = {}
    param_types = []
    variable_counter = {'int': 0, 'float': 0, 'char': 0}


def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR'''
    global current_type
    current_type = p[1]


def p_g_var(p):
    '''g_var : var_declaration'''
    global context, global_var_table, variable_counter
    context = 'local'
    variable_counter = {'int': 0, 'float': 0, 'char': 0}
    print(global_var_table)


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
    global current_id, current_type, current_func, global_var_table, local_var_table, variable_counter, address, counter
    current_id = p[1]
    if context == 'global':
        if current_id not in global_var_table:
            global_var_table[current_id] = (
                current_id, current_type, address['global'][current_type] + counter['global'][current_type], ())
            variable_counter[current_type] += 1
            counter['global'][current_type] += 1
        else:
            print('ERROR: Variable declarada', current_id)
    else:
        if current_id not in local_var_table:
            local_var_table[current_id] = (
                current_id, current_type, address['local'][current_type] + counter['local'][current_type], ())
            variable_counter[current_type] += 1
            counter['local'][current_type] += 1
        else:
            print('ERROR: Variable declarada', current_id)


def p_dec_id1(p):
    '''dec_id1 : L_SB CTE_I R_SB dec_id2
            | empty'''


def p_dec_id2(p):
    '''dec_id2 : L_SB CTE_I R_SB
        | empty'''


def p_id(p):
    '''id : ID id1'''
    global current_id
    current_id = p[1]


def p_id1(p):
    '''id1 : L_SB expression R_SB id2
            | empty'''


def p_id2(p):
    '''id2 : L_SB expression R_SB
        | empty'''


def p_var_type(p):
    '''var_type : type'''


def p_function(p):
    '''function : FUNC func_type ID register_func L_P params R_P var_declaration L_B statements R_B'''
    global current_func, param_types, variable_counter, local_var_table
    dir_func[current_func]['param_types'] = param_types
    dir_func[current_func]['variable_counter'] = variable_counter
    print(local_var_table)
    local_var_table = {}
    param_types = []
    variable_counter = {'int': 0, 'float': 0, 'char': 0}


def p_register_func(p):
    'register_func : '
    global current_func, current_type
    current_func = p[-1]
    if current_func not in dir_func:
        dir_func[current_func] = {'name': current_func, 'type': current_type}
    else:
        print('ERROR: Función declarada', current_func)


def p_func_type(p):
    '''func_type : VOID
                | type'''
    global current_type
    if p[1] != None:
        current_type = p[1]


def p_params(p):
    '''params : var_type param_type dec_id params1
            | empty'''


def p_param_type(p):
    'param_type : '
    global param_types, current_type
    if current_type in ['int', 'float', 'char']:
        param_types.append(current_type)


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
    '''assignation : id id_quad EQUAL expression SEMICOLON'''
    global quadruples, quad_counter, address, counter, elements_stack, types_stack, operators_stack
    right_op = elements_stack.pop()
    right_type = types_stack.pop()
    left_op = elements_stack.pop()
    left_type = types_stack.pop()
    result_type = semantic_cube[left_type]['='][right_type]

    if result_type != None:
        quadruples.append(('=', right_op, None, left_op))
        quad_counter += 1

    else:
        print("ERROR: Type mismatch")


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


def p_call_func_exp(p):
    '''call_func_exp :  ID L_P args R_P'''


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
    '''expression : texp generate_quad op1'''


def p_texp(p):
    '''texp : gexp generate_quad op2'''


def p_gexp(p):
    '''gexp : mexp generate_quad op3aux'''


def p_mexp(p):
    '''mexp : term generate_quad op4aux'''


def p_term(p):
    '''term : fact generate_quad op5aux'''


def p_generate_quad(p):
    '''generate_quad : '''
    global operators_stack
    if not operators_stack.isEmpty() and operators_stack.peek() != '(':
        generate_quadruple()


def p_fact(p):
    '''fact : id id_quad
            | call_func_exp
            | L_P add_fake expression R_P remove_fake
            | cte'''

def p_add_fake(p):
    global operators_stack
    operators_stack.push('(')

def p_add_fake(p):
    global operators_stack
    operators_stack.pop

def p_id_quad(p):
    '''
        id_quad :
    '''
    global elements_stack, types_stack, local_var_table, global_var_table
    element = None
    if current_id in local_var_table:
        element = local_var_table[current_id][2]
    elif current_id in global_var_table:
        element = global_var_table[current_id][2]

    if element != None:
        elements_stack.push(element)
        types_stack.push(current_type)
    else:
        print('ERROR: Undeclared variable')


def p_cte(p):
    '''cte : CTE_F add_cte_float
            | CTE_I add_cte_int
            | CTE_CHAR add_cte_char'''


def p_add_cte_int(p):
    '''add_cte_int : '''
    global elements_stack, types_stack, constant_var_table, address, counter
    cte = p[-1]
    if cte not in constant_var_table:
        constant_var_table[cte] = (
            cte, 'int', address['constant']['int'] + counter['constant']['int'])
        counter['constant']['int'] += 1

    element = constant_var_table[cte][2]

    elements_stack.push(element)
    types_stack.push('int')


def p_add_cte_float(p):
    '''add_cte_float : '''
    global elements_stack, types_stack, constant_var_table, address, counter
    cte = p[-1]
    if cte not in constant_var_table:
        constant_var_table[current_id] = (
            cte, 'float', address['constant']['float'] + counter['constant']['float'])
        counter['constant']['float'] += 1

    element = constant_var_table[cte][2]

    elements_stack.push(element)
    types_stack.push('float')


def p_add_cte_char(p):
    '''add_cte_char : '''
    global elements_stack, types_stack, constant_var_table, address, counter
    cte = p[-1]
    if cte not in constant_var_table:
        constant_var_table[current_id] = (
            cte, 'char', address['constant']['char'] + counter['constant']['char'])
        counter['constant']['char'] += 1

    element = constant_var_table[cte][2]

    elements_stack.push(element)
    types_stack.push('char')


def p_op1(p):
    '''op1 : OR expression
            | empty'''
    global operators_stack
    if p[1] != None:
        operators_stack.push(p[1])


def p_op2(p):
    '''op2 : AND texp
            | empty'''
    global operators_stack
    if p[1] != None:
        operators_stack.push(p[1])


def p_op3(p):
    '''op3 : LESSTHAN
            | LESSTHANEQ 
            | GREATERTHAN
            | GREATERTHANEQ
            | EQ
            | DIFERENT'''
    global operators_stack
    operators_stack.push(p[1])


def p_op3aux(p):
    '''op3aux : op3 mexp
            | empty'''


def p_op4(p):
    '''op4 : PLUS
            | MINUS'''
    global operators_stack
    operators_stack.push(p[1])


def p_op4aux(p):
    '''op4aux : op4 mexp
            | empty'''


def p_op5(p):
    '''op5 : MULT
        | DIV
        | MOD'''
    global operators_stack
    operators_stack.push(p[1])


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


def readFile():
    try:
        file_name = 'test2.txt'
        file = open(file_name, 'r')
        print("Filename used : " + file_name)
        info = file.read()
        file.close()
        lexer.input(info)
        while True:
            tok = lexer.token()
            if not tok:
                break
        yacc.parse(info, tracking=True)
    except EOFError:
        print(EOFError)


readFile()
