import sys
from utils.stack import Stack
from utils.memory_map import Memory
from ast import literal_eval

dir_func = {}
quadruples = []
constant_var_table = {}

func_calls_stack = Stack()
memories_stack = Stack()

global_program_memory = Memory()
new_memory = Memory()
in_ERA = False

GLOBAL_LIMIT = 10000
LOCAL_LIMIT = 27000

counter = {
    "int": 0,
    "float": 0,
    "char": 0
}

# Base address
base_address = {
    "int": 10000,
    "float": 13000,
    "char": 16000
}


def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str


def check_range(address, value_type):
    if value_type == type(1):
        if address in range(1000, 4000) or address in range(10000, 13000):
            return True
        else:
            return False
    elif value_type == type(1.0):
        if address in range(4000, 7000) or address in range(13000, 16000):
            return True
        else:
            return False
    elif value_type == type('a') or value_type == type(True):
        if address in range(7000, 10000) or address in range(16000, 19000):
            return True
        else:
            return False


def get_memory_value(address):
    global global_program_memory
    if address >= GLOBAL_LIMIT and address < LOCAL_LIMIT:
        return memories_stack.peek().get_value(address)
    else:
        return global_program_memory.get_value(address)


def get_value(address):
    if address in range(1000, 4000) or address in range(10000, 13000) or address in range(19000, 21000) or address in range(27000, 30000):
        return int(get_memory_value(address))
    elif address in range(4000, 7000) or address in range(13000, 16000) or address in range(21000, 24000) or address in range(30000, 33000):
        return float(get_memory_value(address))
    elif address in range(7000, 10000) or address in range(16000, 19000) or address in range(24000, 27000) or address in range(33000, 36000):
        return get_memory_value(address)
    else:
        return get_value(get_memory_value(address))


def set_value(value, address):
    global global_program_memory
    if address >= GLOBAL_LIMIT and address < LOCAL_LIMIT:
        memories_stack.peek().set_value(value, address)
    else:
        global_program_memory.set_value(value, address)


def get_result(left_op, op, right_op):
    if(op == '+'):
        return left_op + right_op
    elif(op == '-'):
        return left_op - right_op
    elif(op == '*'):
        return left_op * right_op
    elif(op == '/'):
        return left_op // right_op if isinstance(left_op, int) and isinstance(right_op, int) else left_op / right_op
    elif(op == '%'):
        return left_op % right_op
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
    memories_stack.push(new_memory)

    def igoto():
        global instruction_pointer
        instruction_pointer = third_element
        return instruction_pointer

    def igotoF():
        global instruction_pointer
        first_value = get_value(first_element)
        instruction_pointer = third_element if first_value == 0 else instruction_pointer + 1
        return instruction_pointer

    def iERA():
        global instruction_pointer, new_memory, in_ERA
        new_memory = Memory()
        in_ERA = True
        instruction_pointer += 1
        return instruction_pointer

    def iparam():
        global instruction_pointer, counter, base_address, new_memory
        value = get_value(first_element)
        param_type = dir_func[third_element]['param_types'][second_element]
        address = base_address[param_type] + counter[param_type]
        counter[param_type] += 1
        new_memory.set_value(value, address)
        instruction_pointer += 1
        return instruction_pointer

    def igoSub():
        global instruction_pointer, counter, in_ERA, memories_stack, new_memory
        counter = {
            "int": 0,
            "float": 0,
            "char": 0
        }
        instruction_pointer += 1
        func_calls_stack.push(instruction_pointer)
        in_ERA = False
        memories_stack.push(new_memory)
        instruction_pointer = third_element
        return instruction_pointer

    def iEndFunc():
        global instruction_pointer, memories_stack
        if not memories_stack.is_empty():
            memories_stack.pop()
        if not func_calls_stack.is_empty():
            instruction_pointer = func_calls_stack.pop()
        else:
            instruction_pointer += 1
        return instruction_pointer

    def iprint():
        global instruction_pointer
        print(get_value(third_element))
        instruction_pointer += 1
        return instruction_pointer

    def iread():
        global instruction_pointer
        value = input("Read: ")
        value_type = get_type(value)
        if check_range(third_element, value_type):
            set_value(value, third_element)
            instruction_pointer += 1
        else:
            print('ERROR: Invalid input type', value, third_element)
            sys.exit()
        return instruction_pointer

    def ireturn():
        global instruction_pointer, memories_stack
        value = get_value(third_element)
        current_func = second_element
        memories_stack.pop()
        set_value(value, dir_func[current_func]['memory_address'])
        instruction_pointer = func_calls_stack.pop()
        return instruction_pointer

    def iver():
        global instruction_pointer
        value = get_value(first_element)
        if value in range(third_element):
            instruction_pointer += 1
        else:
            print('ERROR: Index out of bounds', value)
            sys.exit()
        return instruction_pointer

    def iassign():
        global instruction_pointer
        first_value = get_value(first_element)
        set_value(first_value, third_element if third_element <
                  36000 else get_memory_value(third_element))
        instruction_pointer += 1
        return instruction_pointer

    def iexp():
        global instruction_pointer
        first_value = get_value(first_element)
        second_value = get_value(second_element)
        result = get_result(first_value, instruction, second_value)

        set_value(result, third_element)
        instruction_pointer += 1
        return instruction_pointer

    def instruction_error():
        print('ERROR: Wrong instruction')
        sys.exit()

    instruction_switch = {
        'goto': igoto,
        'gotoF': igotoF,
        'goSub': igoSub,
        'param': iparam,
        'ERA': iERA,
        'ENDFunc': iEndFunc,
        'print': iprint,
        'read': iread,
        'return': ireturn,
        'ver': iver,
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
file_name = 'tests/factorial_iter.txt.obj'
with open(file_name, 'r') as file:
    # global dir_func, dir_quadruples
    file_data = eval(file.read())
    dir_func = file_data['dir_func']
    quadruples = file_data['quadruples']
    constant_var_table = file_data['constant_var_table']
    for cte in constant_var_table:
        global_program_memory.set_value(
            constant_var_table[cte][0], constant_var_table[cte][2])
    print(quadruples)
    run()
