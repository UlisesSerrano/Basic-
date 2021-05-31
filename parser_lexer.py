import ply.lex as lex
import ply.yacc as yacc
from utils.stack import Stack
from utils.semantic_cube import semantic_cube

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
    'CTE_I', 'CTE_NEG_I', 'CTE_F', 'CTE_NEG_F','CTE_STRING', 'CTE_CHAR', 'ID', 'SEMICOLON',
    'L_P', 'R_P', 'COMA',
    'L_B', 'R_B',
    'L_SB', 'R_SB',
    'EQUAL', 'GREATERTHAN', 'LESSTHAN',
    'GREATERTHANEQ', 'LESSTHANEQ', 'EQ',
    'DIFERENT', 'AND', 'OR',
    'MINUS', 'PLUS', 'MOD', 'MULT', 'DIV', 'AMP'
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
t_AMP = r'\&'
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

def t_CTE_NEG_F(t):
    r'-\d*\.\d+'
    t.value = float(t.value)
    return t


def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CTE_NEG_I(t):
    r'-\d+'
    t.value = int(t.value)
    return t


def t_CTE_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
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
current_arr_id = ''
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
dim_stack = Stack()
for_id_stack = Stack()

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
    },
    "pointer": 0
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
    },
    "pointer": 36000
}

def clear_parser():
    global current_func,current_arr_id,current_call,current_id,current_for_id,current_type, global_var_table,local_var_table,constant_var_table,dir_func,context,k,types_stack,operators_stack,elements_stack,jumps_stack,dim_stack,for_id_stack,quadruples,counter
    current_type = ''
    current_func = ''
    current_id = ''
    current_for_id = ''
    current_arr_id = ''
    current_call = ''

    global_var_table = {}
    local_var_table = {}
    constant_var_table = {1: (1, 'int', 27000)}
    dir_func = {}
    context = 'global'
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
        },
        "pointer": 0
    }

    k = 0  # Param counter for call_func

    types_stack = Stack()
    operators_stack = Stack()
    elements_stack = Stack()
    jumps_stack = Stack()
    dim_stack = Stack()
    for_id_stack = Stack()

    quadruples = []


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
        print("ERROR: Type mismatch", right_op, op, left_op)


def fill(jump, counter):
    global quadruples
    quadruples[jump][3] = counter


def p_program(p):
    '''program : PROGRAM ID main_quad SEMICOLON g_var funcs main'''
    global dir_func, quadruples, constant_var_table
    print(dir_func)
    print(constant_var_table)
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
    quadruples.append(['ENDFunc', None, None, None])
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
    '''dec_id : ID add_id dec_id1'''


def p_dec_id1(p):
    '''dec_id1 : L_SB CTE_I set_array R_SB dec_id2
            | empty'''


def p_dec_id2(p):
    '''dec_id2 : L_SB CTE_I set_array_2 R_SB
        | empty'''


def p_add_id(p):
    '''add_id : '''
    global current_id, current_type, current_func, global_var_table, local_var_table, address, counter
    current_id = p[-1]
    if context == 'global':
        if current_id not in global_var_table:
            global_var_table[current_id] = [
                current_id, current_type, address['global'][current_type] + counter['global'][current_type], []]
            counter['global'][current_type] += 1
        else:
            print('ERROR: Variable already defined', current_id)
    else:
        if current_id not in local_var_table:
            local_var_table[current_id] = [
                current_id, current_type, address['local'][current_type] + counter['local'][current_type], []]
            counter['local'][current_type] += 1
        else:
            print('ERROR: Variable already defined', current_id)


def p_set_array(p):
    '''set_array : '''
    global current_id, current_type, global_var_table, local_var_table, constant_var_table, address, counter
    cte = p[-1]
    size = p[-1]
    if context == 'global':
        global_var_table[current_id][3].append(size)
        counter['global'][current_type] += size
    else:
        local_var_table[current_id][3].append(size)
        counter['local'][current_type] += size

    if cte not in constant_var_table:
        constant_var_table[cte] = (
            cte, 'int', address['constant']['int'] + counter['constant']['int'])
        counter['constant']['int'] += 1

def p_set_array_2(p):
    '''set_array_2 : '''
    global current_id, current_type, global_var_table, local_var_table, constant_var_table, address, counter
    cte = p[-1]
    size = p[-1]
    if context == 'global':
        global_var_table[current_id][3].append(size)
        prev_size = global_var_table[current_id][3][0]
        counter['global'][current_type] += size * prev_size - prev_size - 1
    else:
        local_var_table[current_id][3].append(size)
        prev_size = local_var_table[current_id][3][0]
        counter['local'][current_type] += size * prev_size - prev_size - 1

    if cte not in constant_var_table:
        constant_var_table[cte] = (
            cte, 'int', address['constant']['int'] + counter['constant']['int'])
        counter['constant']['int'] += 1


def p_id(p):
    '''id : ID set_id id_quad id1'''


def p_set_id(p):
    '''set_id : '''
    global current_id
    current_id = p[-1]


def p_id1(p):
    '''id1 : verify_dim L_SB add_fake expression remove_fake verify_quad_1 R_SB id2 add_base
            | empty'''


def p_id2(p):
    '''id2 : L_SB add_fake expression remove_fake verify_quad_2 R_SB
        | empty'''


def p_verify_dim(p):
    '''verify_dim : '''
    global global_var_table, local_var_table, current_id, current_arr_id, dim_stack
    current_arr_id = current_id
    dim_stack.push({'id': current_arr_id, 'DIM': 1})
    if current_arr_id in local_var_table:
        if len(local_var_table[current_id][3]) == 0:
            print(f'ERROR: Variable {current_id} has not dimensions')
    elif current_arr_id in global_var_table:
        if len(global_var_table[current_id][3]) == 0:
            print(f'ERROR: Variable {current_id} has not dimensions')


def p_verify_quad_1(p):
    '''verify_quad_1 : '''
    global global_var_table, local_var_table, elements_stack, quadruples, current_arr_id, dim_stack, constant_var_table
    dims = []
    first_dim = 0
    current_arr_id = dim_stack.peek()['id']
    if current_arr_id in local_var_table:
        dims = local_var_table[current_arr_id][3]
        first_dim = dims[0]
        quadruples.append(['ver', elements_stack.peek(), None, first_dim])
    elif current_arr_id in global_var_table:
        dims = global_var_table[current_arr_id][3]
        first_dim = dims[0]
        quadruples.append(['ver', elements_stack.peek(), None, first_dim])

    if len(dims) > 1:
        element_op = elements_stack.pop()
        element_type = types_stack.pop()
        result_type = semantic_cube[element_type]['*']['int']

        if result_type != None:
            result = address['temp'][result_type] + \
                counter['temp'][result_type]
            counter['temp'][result_type] += 1

            quadruples.append(['*', element_op, constant_var_table[dims[1]][2], result])

            elements_stack.push(result)
            types_stack.push(result_type)
        else:
            print("ERROR: Type mismatch", element_op, '*', dims[1])



def p_verify_quad_2(p):
    '''verify_quad_2 : '''
    global global_var_table, local_var_table, elements_stack, quadruples, current_arr_id, dim_stack, constant_var_table
    dims = []
    second_dim = 0
    current_arr_id = dim_stack.peek()['id']
    if current_arr_id in local_var_table:
        dims = local_var_table[current_arr_id][3]
        second_dim = dims[1]
        quadruples.append(['ver', elements_stack.peek(), None, second_dim])
    elif current_arr_id in global_var_table:
        dims = global_var_table[current_arr_id][3]
        second_dim = dims[1]
        quadruples.append(['ver', elements_stack.peek(), None, second_dim])

    aux2 = elements_stack.pop()
    type_aux2 = types_stack.pop()
    aux1 = elements_stack.pop()
    type_aux1 = types_stack.pop()
    result_type = semantic_cube[type_aux2]['+'][type_aux1]

    if result_type != None:
        result = address['temp'][result_type] + counter['temp'][result_type]
        counter['temp'][result_type] += 1

        quadruples.append(['+', aux1, aux2, result])

        elements_stack.push(result)
        types_stack.push(result_type)
    else:
        print("ERROR: Type mismatch", aux1, '+', aux2)


def p_add_base(p):
    '''add_base : '''
    global elements_stack, types_stack, address, counter, current_arr_id, global_var_table, local_var_table, current_id
    element_op = elements_stack.pop()
    element_type = types_stack.pop()
    result_type = semantic_cube[element_type]['+']['int']

    base_address = 0
    if result_type != None:
        result = address['pointer'] + counter['pointer']
        counter['pointer'] += 1

        if current_arr_id in local_var_table:
            base_address = local_var_table[current_arr_id][2]
        elif current_arr_id in global_var_table:
            base_address = global_var_table[current_arr_id][2]
        
        if base_address not in constant_var_table:
            constant_var_table[base_address] = (
                base_address, 'int', address['constant']['int'] + counter['constant']['int'])
            counter['constant']['int'] += 1

        quadruples.append(['+', element_op, constant_var_table[base_address][2], result])

        elements_stack.push(result)
        types_stack.push(result_type)
        current_id = current_arr_id
    else:
        print("ERROR: Type mismatch", element_op, '+', base_address)
    
    if not dim_stack.is_empty():
        dim_stack.pop()


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
            memory_address = address['global'][current_type] + counter['global'][current_type]
            global_var_table[current_func] = [current_func, current_type, memory_address,[]]
            counter['global'][current_type] += 1
            dir_func[current_func]['memory_address'] = memory_address
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
    '''assignation : id EQUAL expression SEMICOLON'''
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
    global elements_stack, types_stack, k, dir_func, current_call, counter
    arg_element = elements_stack.pop()
    arg_type = types_stack.pop()

    if k < len(dir_func[current_call]['param_types']):
        if dir_func[current_call]['param_types'][k] == arg_type:
            quadruples.append(['param', arg_element, k, current_call])
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
    '''call_func : AMP ID call_func_era L_P args R_P SEMICOLON'''
    global current_call, dir_func, k, quadruples
    if len(dir_func[current_call]['param_types']) == 0 or k == (len(dir_func[current_call]['param_types'])-1):
        quadruples.append(['goSub', current_call, None,
                           dir_func[current_call]['start_quad']])
    else:
        print('ERROR: Missing arguments', k, len(
            dir_func[current_call]['param_types'])-1)


def p_call_func_exp(p):
    '''call_func_exp : AMP ID call_func_era L_P args R_P'''
    global current_call, dir_func, k
    if len(dir_func[current_call]['param_types']) == 0 or k == (len(dir_func[current_call]['param_types'])-1):
        quadruples.append(['goSub', current_call, None,
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
    global quadruples, elements_stack, types_stack, current_func
    element = elements_stack.pop()
    if types_stack.pop() == dir_func[current_func]['type']:
        quadruples.append(['return', None, current_func, element])
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
    false_jump = jumps_stack.pop()
    jumps_stack.push(len(quadruples)-1)
    fill(false_jump, len(quadruples))


def p_repetition_statement(p):
    '''repetition_statement : while_statement
                            | for_statement'''


def p_for_statement(p):
    '''for_statement : FOR id for_id EQUAL expression for_id_quad TO breadcrumb expression exp_type do_statement'''
    global jumps_stack, quadruples, local_var_table, global_var_table, constant_var_table, current_for_id
    end = jumps_stack.pop()
    element = None
    return_jump = jumps_stack.pop()
    current_for_id = for_id_stack.pop()
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
    global current_for_id, current_id
    for_id_stack.push(current_id)

def p_for_id_quad(p):
    '''for_id_quad : '''
    global quadruples, address, counter, elements_stack, types_stack, current_id, current_for_id
    right_op = elements_stack.pop()
    right_type = types_stack.pop()
    left_op = elements_stack.pop()
    left_type = types_stack.pop()
    result_type = semantic_cube[left_type]['='][right_type]

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
    '''fact : call_func_exp
            | id
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
    is_array = False
    if current_id in local_var_table:
        element = local_var_table[current_id][2]
        element_type = local_var_table[current_id][1]
        is_array = False if len(local_var_table[current_id][3]) == 0 else True
    elif current_id in global_var_table:
        element = global_var_table[current_id][2]
        element_type = global_var_table[current_id][1]
        is_array = False if len(global_var_table[current_id][3]) == 0 else True

    if element != None:
        if not is_array:
            elements_stack.push(element)
            types_stack.push(element_type)
    else:
        print('ERROR: Undeclared variable', current_id)


def p_cte(p):
    '''cte : CTE_CHAR add_cte_char
            | CTE_F add_cte_float
            | CTE_NEG_F add_cte_float
            | CTE_I add_cte_int
            | CTE_NEG_I add_cte_int '''


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
    '''op3aux : op3 gexp
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


def read_file(file_name='test2.txt'):
    clear_parser()
    try:
        file = open(file_name, 'r')
        print("Filename used : " + file_name)
        info = file.read()
        file.close()
        lexer = lex.lex(optimize=1)
        yacc.yacc(optimize = 1)
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
    return file_name
