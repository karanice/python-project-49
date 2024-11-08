from random import randint
from math import gcd as gcd_check


def gcd():
    a = randint(2, 100)
    b = randint(2, 100)

    return str(gcd_check(a, b)), f'{a} {b}'
