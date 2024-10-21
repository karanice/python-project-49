from random import randint
from random import choice


def print_calc():
    print('What is the result of the expression?')


def gen_and_check():
    opers = ['+', '-', '*']
    oper = choice(opers)

    a = randint(2, 20)
    b = randint(2, 20)

    match oper:
        case '+':
            expr = a + b
        case '-':
            expr = a - b
        case '*':
            expr = a * b
    print(f'Question: {a} {oper} {b}')

    return str(expr)
