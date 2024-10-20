from random import randint


def print_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def gen_and_check():
    number = randint(1, 50)
    print(f'Question: {number}')
    return is_even(number)
