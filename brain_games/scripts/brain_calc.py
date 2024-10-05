#!/usr/bin/env python3

from random import randint 
from random import choice
from brain_games.scripts.brain_games import greeting
from brain_games.scripts.procedure import get_name
from brain_games.scripts.procedure import get_answer
from sys import exit


def main():
    greeting()
    user_name = get_name()
    print('What is the result of the expression?')
    opers = ['+', '-', '*']
 

    i = 0
    while i != 3:
        a = randint(0, 20)
        b = randint(0, 20)
        oper = choice(opers)

        match oper:
            case '+':
                expr = a + b
            case '-':
                expr = a - b
            case '*':
                expr = a * b   
        print(f'Question: {a}{oper}{b}')
        user_answer = get_answer()

        if user_answer == str(expr):
            i += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{expr}'")
            print(f'Let\'s try again, {user_name}!')
            exit()
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()