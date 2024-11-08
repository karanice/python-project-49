from random import randint


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even():
    number = randint(1, 50)
    return is_even(number), str(number)
