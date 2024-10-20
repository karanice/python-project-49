from random import randint


def print_gcd():
    print('Find the greatest common divisor of given numbers.')


def gen_and_check():
    a = randint(2, 100)
    b = randint(2, 100)

    print(f'Question: {a} {b}')

    if a < b:
        a, b = b, a

    while a % b != 0:
        a = a % b
        a, b = b, a

    return str(b)
