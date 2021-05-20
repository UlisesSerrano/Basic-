import sys
import ply.lex as lex
import ply.yacc as yacc
from stack import Stack
from semantic_cube import semantic_cube
from kivy.app import App
from kivy.extras.highlight import KivyLexer
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.behaviors import EmacsBehavior
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
from pygments import lexers
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import codecs
import os

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
    'CTE_I', 'CTE_F', 'CTE_STRING', 'CTE_CHAR', 'ID', 'SEMICOLON',
    'L_P', 'R_P', 'COMA',
    'L_B', 'R_B',
    'L_SB', 'R_SB',
    'EQUAL', 'GREATERTHAN', 'LESSTHAN',
    'GREATERTHANEQ', 'LESSTHANEQ', 'EQ',
    'DIFERENT', 'AND', 'OR',
    'MINUS', 'PLUS', 'MOD', 'MULT', 'DIV',
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
    r'\"([^\\\n]|(\\.))*?\"'
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
current_for_id = ''
current_call = ''

global_var_table = {}
local_var_table = {}
constant_var_table = {1: (1, 'int', 27000)}
dir_func = {}
context = 'global'

param_types = []
k = 0  # Param counter for call_func

types_stack = Stack()
operators_stack = Stack()
elements_stack = Stack()
jumps_stack = Stack()

quadruples = []

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
        "int": 1,
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
    global quadruples, address, counter, elements_stack, types_stack, operators_stack
    right_op = elements_stack.pop()
    right_type = types_stack.pop()
    left_op = elements_stack.pop()
    left_type = types_stack.pop()
    op = operators_stack.pop()
    result_type = semantic_cube[left_type][op][right_type]

    if result_type != None:
        result = address['temp'][result_type] + counter['temp'][result_type]
        counter['temp'][result_type] += 1

        quadruples.append([op, left_op, right_op, result])

        elements_stack.push(result)
        types_stack.push(result_type)

    else:
        print("ERROR: Type mismatch quad", right_op, op, left_op)


def fill(jump, counter):
    global quadruples
    quadruples[jump][3] = counter


def p_program(p):
    '''program : PROGRAM ID main_quad SEMICOLON g_var funcs main'''
    global dir_func, quadruples
    print(dir_func)
    print(quadruples)


def p_main_quad(p):
    '''main_quad : '''
    global quadruples
    quadruples.append(['goto', None, None, None])


def p_main(p):
    '''main : MAIN L_P params R_P var_declaration L_B main_start statements R_B'''
    global local_var_table, param_types, counter, dir_func
    current_func = 'main'
    if current_func not in dir_func:
        dir_func[current_func] = {'name': current_func, 'type': 'void', 'param_types': param_types, 'variable_counter': {
            'local': counter['local'], 'temp': counter['temp']}}
    else:
        print('ERROR: Function already defined', current_func)

    print(local_var_table)
    local_var_table = {}
    param_types = []
    counter['local'] = {'int': 0, 'float': 0, 'char': 0}
    counter['temp'] = {'int': 0, 'float': 0, 'char': 0}


def p_main_start(p):
    '''main_start : '''
    fill(0, len(quadruples))


def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR'''
    global current_type
    current_type = p[1]


def p_g_var(p):
    '''g_var : var_declaration'''
    global context, global_var_table
    context = 'local'
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
    global current_id, current_type, current_func, global_var_table, local_var_table, address, counter
    current_id = p[1]
    if context == 'global':
        if current_id not in global_var_table:
            global_var_table[current_id] = (
                current_id, current_type, address['global'][current_type] + counter['global'][current_type], ())
            counter['global'][current_type] += 1
        else:
            print('ERROR: Variable already defined', current_id)
    else:
        if current_id not in local_var_table:
            local_var_table[current_id] = (
                current_id, current_type, address['local'][current_type] + counter['local'][current_type], ())
            counter['local'][current_type] += 1
        else:
            print('ERROR: Variable already defined', current_id)


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
    '''function : FUNC func_type ID register_func L_P params R_P add_params var_declaration start_func L_B statements R_B'''
    global current_func, param_types, local_var_table, counter
    dir_func[current_func]['param_types'] = param_types
    dir_func[current_func]['variable_counter'] = {
        'local': counter['local'], 'temp': counter['temp']}
    print(local_var_table)
    local_var_table = {}
    quadruples.append(['ENDFunc', None, None, None])
    param_types = []
    counter['local'] = {'int': 0, 'float': 0, 'char': 0}
    counter['temp'] = {'int': 0, 'float': 0, 'char': 0}


def p_register_func(p):
    'register_func : '
    global current_func, current_type, dir_func, address, counter
    current_func = p[-1]
    if current_func not in dir_func:
        dir_func[current_func] = {'name': current_func, 'type': current_type}
        if (current_type != 'void'):
            global_var_table[current_func] = (
                current_func, current_type, address['global'][current_type] + counter['global'][current_type], ())
            counter['global'][current_type] += 1
    else:
        print('ERROR: Function already defined', current_func)


def p_add_params(p):
    'add_params : '
    global current_func, param_types, dir_func
    dir_func[current_func]['param_types'] = param_types


def p_start_func(p):
    'start_func : '
    global current_func, dir_func, quadruples
    dir_func[current_func]['start_quad'] = len(quadruples)


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
    global quadruples, address, counter, elements_stack, types_stack
    right_op = elements_stack.pop()
    right_type = types_stack.pop()
    left_op = elements_stack.pop()
    left_type = types_stack.pop()
    result_type = semantic_cube[left_type]['='][right_type]

    if result_type != None:
        quadruples.append(['=', right_op, None, left_op])
    else:
        print("ERROR: Type mismatch in assignation")


def p_args(p):
    '''args : args1
            | empty'''


def p_args1(p):
    'args1 : add_fake expression param_check remove_fake args2'


def p_param_check(p):
    '''param_check : '''
    global elements_stack, types_stack, k, dir_func, current_call
    arg_element = elements_stack.pop()
    arg_type = types_stack.pop()

    if k < len(dir_func[current_call]['param_types']):
        if dir_func[current_call]['param_types'][k] == arg_type:
            quadruples.append(['PARAM', arg_element, k, None])
        else:
            print('ERROR: Type mismatch on argument on call function', current_call)
    else:
        print('ERROR: Incorrect number of arguments', current_call)


def p_args2(p):
    '''args2 : COMA next_arg args1
            | empty'''


def p_next_arg(p):
    '''next_arg : '''
    global k
    k += 1


def p_call_func(p):
    '''call_func :  ID call_func_era L_P args R_P SEMICOLON'''
    global current_call, dir_func, k, quadruples
    if k == (len(dir_func[current_call]['param_types'])-1):
        quadruples.append(['GOSUB', current_call, None,
                           dir_func[current_call]['start_quad']])
    else:
        print('ERROR: Missing arguments', k, len(
            dir_func[current_call]['param_types'])-1)


def p_call_func_exp(p):
    '''call_func_exp :  ID call_func_era L_P args R_P'''
    global current_call, dir_func, k
    if k == (len(dir_func[current_call]['param_types'])-1):
        quadruples.append(['GOSUB', current_call, None,
                           dir_func[current_call]['start_quad']])
        if current_call in global_var_table:
            func_var = global_var_table[current_call]
            func_temp_add = address['temp'][func_var[1]] + \
                counter['temp'][func_var[1]]
            counter['temp'][func_var[1]] += 1

            quadruples.append(['=', func_var[2], None, func_temp_add])

            elements_stack.push(func_temp_add)
            types_stack.push(func_var[1])
        else:
            print('ERROR: Cannot call void function on expresion', current_call)
    else:
        print('ERROR: Missing arguments', k, len(
            dir_func[current_call]['param_types'])-1)


def p_call_func_era(p):
    '''call_func_era : '''
    global dir_func, quadruples, k, current_call
    if p[-1] in dir_func:
        current_call = p[-1]
        quadruples.append(['ERA', current_call, None, None])
        k = 0
    else:
        print('ERROR: Undeclared function', p[-1])


def p_return_func(p):
    '''return_func : RETURN L_P expression R_P SEMICOLON'''
    global quadruples, elements_stack, types_stack, global_var_table, current_func
    element = elements_stack.pop()
    if types_stack.pop() == dir_func[current_func]['type']:
        quadruples.append(['return', None, None, element])
    else:
        print('ERROR: Return type mismatch')


def p_read(p):
    '''read : READ L_P read_args R_P SEMICOLON'''
    global quadruples, elements_stack, types_stack
    element = elements_stack.pop()
    types_stack.pop()

    quadruples.append(['read', None, None, element])


def p_read_args(p):
    '''read_args : add_fake expression remove_fake read_args1'''


def p_read_args1(p):
    '''read_args1 : COMA add_fake expression remove_fake read_args1
                | empty'''


def p_write(p):
    '''write : PRINT L_P write_args R_P SEMICOLON'''


def p_write_args(p):
    '''write_args : write_args2 write_args1'''


def p_write_args1(p):
    '''write_args1 : COMA write_args2 write_args1
                    | empty'''


def p_write_args2(p):
    '''write_args2 : add_fake expression remove_fake
                | CTE_STRING add_cte_string'''
    global quadruples, elements_stack, types_stack
    element = elements_stack.pop()
    types_stack.pop()
    quadruples.append(['print', None, None, element])


def p_decision_statement(p):
    '''decision_statement : IF L_P expression R_P exp_type L_B statements R_B decision_statement1'''
    global jumps_stack, quadruples
    end = jumps_stack.pop()
    fill(end, len(quadruples))


def p_decision_statement1(p):
    '''decision_statement1 : ELSE else_jump L_B statements R_B
                            | empty'''


def p_exp_type(p):
    '''exp_type : '''
    global types_stack, elements_stack, jumps_stack, quadruples
    exp_type = types_stack.pop()
    if exp_type == 'int':
        result = elements_stack.pop()
        quadruples.append(['gotoF', result, None, None])
        jumps_stack.push(len(quadruples)-1)
    else:
        print('ERROR: Type mismatch')


def p_else_jump(p):
    '''else_jump : '''
    global quadruples, jumps_stack
    quadruples.append(['goto', None, None, None])
    false = jumps_stack.pop()
    jumps_stack.push(len(quadruples)-1)
    fill(false, len(quadruples))


def p_repetition_statement(p):
    '''repetition_statement : while_statement
                            | for_statement'''


def p_for_statement(p):
    '''for_statement : FOR id id_quad EQUAL expression for_id TO breadcrumb expression exp_type do_statement'''
    global jumps_stack, quadruples, local_var_table, global_var_table, constant_var_table, current_for_id
    end = jumps_stack.pop()
    element = None
    return_jump = jumps_stack.pop()
    if current_for_id in local_var_table:
        element = local_var_table[current_for_id][2]
        id_type = local_var_table[current_for_id][1]
    elif current_for_id in global_var_table:
        element = global_var_table[current_for_id][2]
        id_type = global_var_table[current_for_id][1]

    if element != None:
        result_type = semantic_cube[id_type]['+']['int']
        if result_type != None:
            quadruples.append(
                ['+', element, constant_var_table[1][2], element])
        else:
            print("ERROR: Type mismatch")
    else:
        print('ERROR: Undeclared variable', current_for_id)
    quadruples.append(['goto', None, None, return_jump])
    fill(end, len(quadruples))


def p_for_id(p):
    '''for_id : '''
    global quadruples, address, counter, elements_stack, types_stack, current_id, current_for_id
    right_op = elements_stack.pop()
    right_type = types_stack.pop()
    left_op = elements_stack.pop()
    left_type = types_stack.pop()
    result_type = semantic_cube[left_type]['='][right_type]
    current_for_id = current_id

    if result_type != None:
        quadruples.append(['=', right_op, None, left_op])
    else:
        print("ERROR: Type mismatch on loop id")


def p_breadcrumb(p):
    '''breadcrumb : '''
    global jumps_stack, quadruples
    jumps_stack.push(len(quadruples))


def p_while_statement(p):
    '''while_statement : WHILE L_P breadcrumb expression R_P exp_type do_statement'''
    global jumps_stack, quadruples
    end = jumps_stack.pop()
    return_jump = jumps_stack.pop()
    quadruples.append(['goto', None, None, return_jump])
    fill(end, len(quadruples))


def p_do_statement(p):
    '''do_statement :  DO L_B statements R_B'''


def p_expression(p):
    '''expression : texp generate_quad_1 op1'''


def p_texp(p):
    '''texp : gexp generate_quad_2 op2'''


def p_gexp(p):
    '''gexp : mexp generate_quad_3 op3aux'''


def p_mexp(p):
    '''mexp : term generate_quad_4 op4aux'''


def p_term(p):
    '''term : fact generate_quad_5 op5aux'''


def p_generate_quad_1(p):
    '''generate_quad_1 : '''
    global operators_stack
    if not operators_stack.is_empty() and operators_stack.peek() != '(' and operators_stack.peek() == '||':
        generate_quadruple()


def p_generate_quad_2(p):
    '''generate_quad_2 : '''
    global operators_stack
    if not operators_stack.is_empty() and operators_stack.peek() != '(' and operators_stack.peek() == '&&':
        generate_quadruple()


def p_generate_quad_3(p):
    '''generate_quad_3 : '''
    global operators_stack
    if not operators_stack.is_empty() and operators_stack.peek() != '(' and operators_stack.peek() in ['<', '>', '<=', '>=', '!=', '==']:
        generate_quadruple()


def p_generate_quad_4(p):
    '''generate_quad_4 : '''
    global operators_stack
    if not operators_stack.is_empty() and operators_stack.peek() != '(' and operators_stack.peek() in ['+', '-']:
        generate_quadruple()


def p_generate_quad_5(p):
    '''generate_quad_5 : '''
    global operators_stack
    if not operators_stack.is_empty() and operators_stack.peek() != '(' and operators_stack.peek() in ['*', '/', '%']:
        generate_quadruple()


def p_fact(p):
    '''fact : id id_quad
            | call_func_exp
            | L_P add_fake expression R_P remove_fake
            | cte'''


def p_add_fake(p):
    '''add_fake : '''
    global operators_stack
    operators_stack.push('(')


def p_remove_fake(p):
    '''remove_fake : '''
    global operators_stack
    operators_stack.pop()


def p_id_quad(p):
    '''
        id_quad :
    '''
    global elements_stack, types_stack, local_var_table, global_var_table, current_id
    element = None
    element_type = None
    if current_id in local_var_table:
        element = local_var_table[current_id][2]
        element_type = local_var_table[current_id][1]
    elif current_id in global_var_table:
        element = global_var_table[current_id][2]
        element_type = global_var_table[current_id][1]

    if element != None:
        elements_stack.push(element)
        types_stack.push(element_type)
    else:
        print('ERROR: Undeclared variable', current_id)


def p_cte(p):
    '''cte : CTE_CHAR add_cte_char
            | CTE_F add_cte_float
            | CTE_I add_cte_int '''


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
        constant_var_table[cte] = (
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
        constant_var_table[cte] = (
            cte, 'char', address['constant']['char'] + counter['constant']['char'])
        counter['constant']['char'] += 1

    element = constant_var_table[cte][2]

    elements_stack.push(element)
    types_stack.push('char')

def p_add_cte_string(p):
    '''add_cte_string : '''
    global elements_stack, types_stack, constant_var_table, address, counter
    cte = p[-1]
    if cte not in constant_var_table:
        constant_var_table[cte] = (
            cte, 'char', address['constant']['char'] + counter['constant']['char'])
        counter['constant']['char'] += 1

    element = constant_var_table[cte][2]

    elements_stack.push(element)
    types_stack.push('char')

def p_add_operator(p):
    '''add_operator : '''
    global operators_stack
    operators_stack.push(p[-1])

def p_op1(p):
    '''op1 : OR add_operator expression
            | empty'''

def p_op2(p):
    '''op2 : AND add_operator texp
            | empty'''


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
        export = {
            'dir_func': dir_func,
            'quadruples': quadruples,
            'constant_var_table': constant_var_table
        }
        with open(file_name + '.obj', 'w') as file1:
            file1.write(str(export))

    except EOFError:
        print(EOFError)


readFile()


example_text = '''
---------------------Python----------------------------------
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        return Button(text='Hello World')
if __name__ == '__main__':
    MyApp().run()
----------------------Java-----------------------------------
public static byte toUnsignedByte(int intVal) {
    byte byteVal;
    return (byte)(intVal & 0xFF);
}
---------------------kv lang---------------------------------
#:kivy 1.0
<YourWidget>:
    canvas:
        Color:
            rgb: .5, .5, .5
        Rectangle:
            pos: self.pos
            size: self.size
---------------------HTML------------------------------------
<!-- Place this tag where you want the +1 button to render. -->
<div class="g-plusone" data-annotation="inline" data-width="300"></div>
<!-- Place this tag after the last +1 button tag. -->
<script type="text/javascript">
  (function() {
    var po = document.createElement('script');
    po.type = 'text/javascript';
    po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(po, s);
  })();
</script>
----------------------Emacs key bindings---------------------
This CodeInput inherits from EmacsBehavior, so you can use Emacs key bindings
if you want! To try out Emacs key bindings, set the "Key bindings" option to
"Emacs". Experiment with the shortcuts below on some of the text in this window
(just be careful not to delete the cheat sheet before you have made note of the
commands!)
Shortcut           Description
--------           -----------
Control + a        Move cursor to the beginning of the line
Control + e        Move cursor to the end of the line
Control + f        Move cursor one character to the right
Control + b        Move cursor one character to the left
Alt + f            Move cursor to the end of the word to the right
Alt + b            Move cursor to the start of the word to the left
Alt + Backspace    Delete text left of the cursor to the beginning of word
Alt + d            Delete text right of the cursor to the end of the word
Alt + w            Copy selection
Control + w        Cut selection
Control + y        Paste selection

print(10*5);
string name = input_s();
print("String input: " + name);
int i = input_i();
print("Int input: ");
print(i);
float f = input_f();
'''


class Fnt_SpinnerOption(SpinnerOption):
    pass


class LoadDialog(Popup):

    def load(self, path, selection):
        self.choosen_file = [None, ]
        self.choosen_file = selection
        Window.title = selection[0][selection[0].rfind(os.sep) + 1:]
        self.dismiss()

    def cancel(self):
        self.dismiss()


class SaveDialog(Popup):

    def save(self, path, selection):
        _file = codecs.open(selection, 'w', encoding='utf8')
        _file.write(self.text)
        Window.title = selection[selection.rfind(os.sep) + 1:]
        _file.close()
        self.dismiss()

    def cancel(self):
        self.dismiss()


class CodeInputWithBindings(EmacsBehavior, CodeInput):

    '''CodeInput with keybindings.
    To add more bindings, add the behavior before CodeInput in the class
    definition.
    '''
    pass


class main(App):

    files = ListProperty([None, ])

    def build(self):
        b = BoxLayout(orientation='vertical')
        languages = Spinner(
            text='language',
            values=sorted(['KvLexer', ] + list(lexers.LEXERS.keys())))

        languages.bind(text=self.change_lang)

        menu = BoxLayout(
            size_hint_y=None,
            height='15pt')
        fnt_size = Spinner(
            text='20',
            values=list(map(str, list(range(15, 45, 5)))))
        fnt_size.bind(text=self._update_size)

        fonts = [
            file for file in LabelBase._font_dirs_files
            if file.endswith('.ttf')]

        fnt_name = Spinner(
            text='Courier New',
            option_cls=Fnt_SpinnerOption,
            values=fonts)
        fnt_name.bind(text=self._update_font)
        mnu_file = Spinner(
            text='File',
            values=('Open', 'SaveAs', 'Save', 'Close'))
        mnu_file.bind(text=self._file_menu_selected)
        key_bindings = Spinner(
            text='Key bindings',
            values=('Default key bindings', 'Emacs key bindings'))
        key_bindings.bind(text=self._bindings_selected)

        run_button = Button(text='Run')

        menu.add_widget(mnu_file)
        menu.add_widget(fnt_size)
        menu.add_widget(run_button)
        b.add_widget(menu)

        self.codeinput = CodeInputWithBindings(
            lexer=KivyLexer(),
            font_size=20,
            text=example_text,
            key_bindings='default',
        )
        self.output = CodeInputWithBindings(
            font_size=20,
            text= "SECTION: OUTPUT\n",
            foreground_color=(1,1,1,1),
            background_color= (0,0,0,0.5),
            key_bindings='default',
        )
        self.text_input = TextInput(foreground_color=(1,1,1,1),background_color=(0,0,0,0.25),text='Hello world', multiline=False)
        self.text_input.bind(on_text_validate=self.on_enter)

        b.add_widget(self.codeinput)
        b.add_widget(self.text_input)
        b.add_widget(self.output)

        return b

    def _update_size(self, instance, size):
        self.codeinput.font_size = float(size)

    def _update_font(self, instance, fnt_name):
        instance.font_name = self.codeinput.font_name = fnt_name

    def _file_menu_selected(self, instance, value):
        if value == 'File':
            return
        instance.text = 'File'
        if value == 'Open':
            if not hasattr(self, 'load_dialog'):
                self.load_dialog = LoadDialog()
            self.load_dialog.open()
            self.load_dialog.bind(choosen_file=self.setter('files'))
        elif value == 'SaveAs':
            if not hasattr(self, 'saveas_dialog'):
                self.saveas_dialog = SaveDialog()
            self.saveas_dialog.text = self.codeinput.text
            self.saveas_dialog.open()
        elif value == 'Save':
            if self.files[0]:
                _file = codecs.open(self.files[0], 'w', encoding='utf8')
                _file.write(self.codeinput.text)
                _file.close()
        elif value == 'Close':
            if self.files[0]:
                self.codeinput.text = ''
                Window.title = 'untitled'
    def on_enter(self, instance):
      self.stdin = instance.text
      self.display_output(f'{self.stdin}\n')
      self.resume_vm_execution()

    def _bindings_selected(self, instance, value):
        value = value.split(' ')[0]
        self.codeinput.key_bindings = value.lower()

    def on_files(self, instance, values):
        if not values[0]:
            return
        _file = codecs.open(values[0], 'r', encoding='utf8')
        self.codeinput.text = _file.read()
        _file.close()

    def change_lang(self, instance, z):
        if z == 'KvLexer':
            lx = KivyLexer()
        else:
            lx = lexers.get_lexer_by_name(lexers.LEXERS[z][2][0])
        self.codeinput.lexer = lx


if __name__ == '__main__':
    main().run()
