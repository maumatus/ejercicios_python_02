print('Calculadora chucheta Luty y sus amiguitas')


def add(x, y):
    # Adds two numbers
    return x + y


def subtract(x, y):
    # Substracts two numbers
    return x - y


def multiply(x, y):
    # Multiply two numbers
    return x * y


def divide(x, y):
    # Divide two numbers
    return x / y


def check_if_user_has_finished():
    # Checks that the user wants to finish or not.
    # Performs some verification of the input.
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Quieres terminar (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Respuesta debe ser (y/n)')
    return ok_to_finish


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Elige un menú:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('\t5. Modulus')
        print('\t6. Power of')
        print('--------------------')
        user_selection = input('Elige un número:')
        if user_selection in ('1', '2', '3', '4', '5', '6'):
            input_ok = True
        else:
            print('Error (debe seleccionar un número 1 - 5)')
    print('-----------------')
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input(float('Ingresa primer numero: '))
    num2 = get_integer_input(float('Ingresa segundo numero: '))
    return num1, num2


def get_float_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('El numero debe ser en decimales')
        value_as_string = input(message)
    return int(float(value_as_string))


finished = False


while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 =  get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice =='2':
        result = subtract(n1, n2)
    elif menu_choice =='3':
        result = multiply(n1, n2)
    elif menu_choice ==  '4':
        result = divide(n1, n2)
    print('Result:', result)
    print('=================')
    finished = check_if_user_has_finished()


print('Nos vemos en el infierno')




