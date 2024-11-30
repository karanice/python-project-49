import random
from brain_games.engine.engine import run_game
from brain_games.consts import CALC_INSTRUCTION
from brain_games.utils import get_random_number


def get_random_operator(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])


def get_question_and_answer():
    first_num, second_num = get_random_number(), get_random_number()
    sign, result = get_random_operator(first_num, second_num)
    question = f'{first_num} {sign} {second_num}'
    return question, result


def run_calc_game():
    run_game(get_question_and_answer, CALC_INSTRUCTION)
