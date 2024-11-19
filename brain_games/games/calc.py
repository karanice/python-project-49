import random
from brain_games.engine.engine import run_game
from brain_games.consts import CALC_INSTRUCTION
from brain_games.utils import get_random_number


def rand_oper(a, b):
    return random.choice(list({
        '+': a + b,
        '-': a - b,
        '*': a * b
    }.items()))


def get_question_and_answer():
    a, b = get_random_number(), get_random_number()
    sign, result = rand_oper(a, b)
    question = f'{a} {sign} {b}'
    return question, str(result)


def run_calc_game():
    run_game(get_question_and_answer, CALC_INSTRUCTION)
