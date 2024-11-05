from random import randint
from math import sqrt


def print_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


# number > 2
def is_prime(number):
    flag = True
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            flag = False
    return 'yes' if flag else 'no'


def gen_and_check():
    number = randint(3, 300)
    print(f'Question: {number}')
    return is_prime(number)
