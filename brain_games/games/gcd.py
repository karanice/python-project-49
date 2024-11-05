from random import randint
from math import gcd


def gen_and_check():
    a = randint(2, 100)
    b = randint(2, 100)

    print(f'Question: {a} {b}')

    return str(gcd(a, b))
