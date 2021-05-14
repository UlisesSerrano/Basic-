from stack import Stack
from memory_map import Memory

dir_func = {}
quadruples = []
constant_var_table = {}

func_calls_stack = Stack()
memories_stack = Stack()

program_memory = Memory()


def get_memory_value(address):
    global program_memory
    return program_memory.get_value(address)


def get_value(address):
    return get_memory_value(address)


def set_value(value, address):
    global program_memory
    return program_memory.set_value(value, address)


def get_result(left_op, op, right_op):
    if(op == '+'):
        return left_op + right_op
    elif(op == '-'):
        return left_op - right_op
    elif(op == '*'):
        return left_op * right_op
    elif(op == '/'):
        return left_op // right_op if isinstance(left_op, int) and isinstance(right_op, int) else left_op / right_op
    elif(op == '<'):
        return left_op < right_op
    elif(op == '<='):
        return left_op <= right_op
    elif(op == '>'):
        return left_op > right_op
    elif(op == '>='):
        return left_op >= right_op
    elif(op == '=='):
        return left_op == right_op
    elif(op == '!='):
        return left_op != right_op
    elif(op == '&&'):
        return 1 if left_op and right_op else 0
    elif(op == '||'):
        return 1 if left_op or right_op else 0


def run():
    instruction_pointer = 0
    current_quad = quadruples[instruction_pointer]
    instruction = ''
    first_element = 0
    second_element = 0
    third_element = 0

    def igoto():
        global instruction_pointer
        instruction_pointer = third_element
        return instruction_pointer

    def igotoF():
        global instruction_pointer
        first_value = get_value(first_element)
        instruction_pointer = third_element if first_value == 0 else instruction_pointer + 1
        return instruction_pointer

    def iprint():
        global instruction_pointer
        print(get_value(third_element))
        instruction_pointer += 1
        return instruction_pointer

    def iread():
        global instruction_pointer
        value = input()
        set_value(value, third_element)
        instruction_pointer += 1
        return instruction_pointer

    def ireturn():
        global instruction_pointer
        value = get_value(third_element)
        return instruction_pointer

    def iassign():
        global instruction_pointer
        first_value = get_value(first_element)
        set_value(first_value, third_element)
        instruction_pointer += 1
        return instruction_pointer

    def iexp():
        global instruction_pointer
        first_value = get_value(first_element)
        second_value = get_value(second_element)
        result = get_result(first_value, instruction, second_value)
        set_value(result, third_element)
        print(result, third_element)
        instruction_pointer += 1
        return instruction_pointer

    def instruction_error():
        print('ERROR: Wrong instruction')

    instruction_switch = {
        'goto': igoto,
        'gotoF': igotoF,
        'print': iprint,
        'read': iread,
        'return': ireturn,
        '=': iassign,
        '+': iexp,
        '-': iexp,
        '*': iexp,
        '/': iexp,
        '%': iexp,
        '<': iexp,
        '>': iexp,
        '<=': iexp,
        '>=': iexp,
        '!=': iexp,
        '==': iexp,
        '&&': iexp,
        '||': iexp,
    }

    while instruction_pointer < len(quadruples):
        current_quad = quadruples[instruction_pointer]
        instruction = current_quad[0]
        first_element = current_quad[1]
        second_element = current_quad[2]
        third_element = current_quad[3]

        instruction_pointer = instruction_switch.get(
            instruction, instruction_error)()


# Compile program.
file_name = 'test2.txt.obj'
with open(file_name, 'r') as file:
    #global dir_func, dir_quadruples
    file_data = eval(file.read())
    dir_func = file_data['dir_func']
    quadruples = file_data['quadruples']
    constant_var_table = file_data['constant_var_table']
    for cte in constant_var_table:
        program_memory.set_value(
            constant_var_table[cte][0], constant_var_table[cte][2])
    print(quadruples)
    run()
