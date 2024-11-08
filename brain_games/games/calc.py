from random import randint
from random import choice
from operator import add, sub, mul


def calc():
    a = randint(2, 20)
    b = randint(2, 20)
    exps = {
        '+': add(a, b),
        '-': sub(a, b),
        '*': mul(a, b)
    }
    oper = choice(list(exps.keys()))

    return str(exps[oper]), f'{a} {oper} {b}'
