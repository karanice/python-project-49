from random import randint


def progression():
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

    return check, " ".join(row)
