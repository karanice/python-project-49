from random import randint


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def gen_and_check():
    number = randint(1, 50)
    print(f'Question: {number}')
    return is_even(number)
