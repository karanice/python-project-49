import prompt
from brain_games.consts import ROUND_NUMBERS


def run_game(get_question_and_answer, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{instruction}')

    for round in range(0, ROUND_NUMBERS):
        question, check = get_question_and_answer()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')

        if user_answer == check:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{check}\n'"
                  f"Let\'s try again, {name}!")
            return None

    print(f'Congratulations, {name}!')
