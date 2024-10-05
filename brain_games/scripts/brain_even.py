#!/usr/bin/env python3

from random import randint
from brain_games.scripts.brain_games import greeting
from brain_games.scripts.procedure import get_name
from brain_games.scripts.procedure import get_answer
from sys import exit


def is_even(number): ### специфическая для игры функция
    return 'yes' if number % 2 == 0 else 'no'


def main():
    greeting()
    user_name = get_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i != 3:
        number = randint(0,50) ### вот это место заменить
        parity_check = is_even(number) ### модульной функцией
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
