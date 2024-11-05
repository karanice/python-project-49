from random import randint
from random import choice
from operator import add, sub, mul


def gen():
    a = randint(2, 20)
    b = randint(2, 20)
    exps = {
        '+': add(a, b),
        '-': sub(a, b),
        '*': mul(a, b)
    }
    oper = choice(list(exps.keys()))
    return a, b, oper, exps[oper]


def check():
    a, b, oper, exp = gen()
    print(f'Question: {a} {oper} {b}')
    return str(exp)
