from random import randint


def print_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number): # number > 2
    for i in range (2, number//2):
        if number % i == 0:
            return 'no'
    
    return 'yes'


def gen_and_check():
    number = randint(3,300)
    print(f'Question: {number}')
    return is_prime(number)