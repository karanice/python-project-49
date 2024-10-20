#!/usr/bin/env python3

from random import randint
from brain_games.scripts.brain_games import greeting
from brain_games.scripts.procedure import get_name
from brain_games.scripts.procedure import get_answer
from brain_games.games.even import print_even
from brain_games.games.even import gen_and_check

from sys import exit

def main():
    greeting()
    user_name = get_name()
    print_even()
    i = 0
    while i != 3:
        number, check = gen_and_check()
        print(f'Question: {number}')
        user_answer = get_answer()

        if user_answer == check:
            i += 1
            print('Correct!')
        else:
            i = 0
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{user_name}'")
            print(f'Let\'s try again, {user_name}!')
            exit()


    print(f'Congratulations, {user_name}!')

if __name__ == '__main__':
    main()
