#!/usr/bin/env python3

from random import randint
from brain_games.scripts.brain_games import greeting
from sys import exit

def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_name():
    name = ''
    while name == '':
        name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    answer = ''
    while answer == '':
        answer = input('Your answer: ')
    return answer


def main():
    greeting()
    user_name = get_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i != 3:
        number = randint(0,50)
        parity_check = is_even(number)
        print(f'Question: {number}')
        user_answer = get_answer()

        if user_answer == parity_check:
            i += 1
            print('Correct!')
        else:
            i = 0
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{parity_check}'")
            print(f'Let\'s try again, {user_name}!')
            exit()


    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
