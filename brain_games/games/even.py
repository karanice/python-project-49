from random import randint

def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'

def print_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')

def gen_and_check():
    number = randint(0,50)
    parity_check = is_even(number)
    check = parity_check
    return number, check