from random import randint
from math import sqrt


# number > 2
def is_prime(number):
    flag = True
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            flag = False

    return 'yes' if flag else 'no'


def prime():
    number = randint(3, 300)

    return is_prime(number), str(number)
