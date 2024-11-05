from random import randint


def print_progression():
    print('What number is missing in the progression?')


def gen_and_check():
    number = randint(2, 9)
    step = randint(-5, 5)

    row = []
    dots = randint(0, 9)
    check = str(number + step * dots)

    for i in range(0, 10):
        el = str(number)
        row.append('..') if i == dots else row.append(el)
        number += step
        i += 1

    print(f'Question: {" ".join(row)}')

    return check
