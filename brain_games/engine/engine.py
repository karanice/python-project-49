from brain_games.scripts.brain_games import greeting
from sys import exit
from prompt import string


def procedure(do_check, instruction):
    greeting()
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}')

    print(instruction)

    i = 0
    for i in range(0, 3):
        check, question = do_check()
        print('Question: ' + question)
        user_answer = string('Your answer: ')

        if user_answer == check:
            i += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{check}'")
            print(f'Let\'s try again, {user_name}!')
            exit()

    print(f'Congratulations, {user_name}!')
