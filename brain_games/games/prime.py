from random import randint


def print_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


# number > 2
def is_prime(number):
    for i in range(2, number//2):
        if number % i == 0:
            return 'no'

    return 'yes'


def gen_and_check():
    number = randint(3, 300)
    print(f'Question: {number}')
    return is_prime(number)
