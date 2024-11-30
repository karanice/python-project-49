from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine.engine import run_game
from brain_games.utils import get_random_number


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    problem_num = get_random_number()
    answer = 'yes' if is_even(problem_num) else 'no'

    return problem_num, answer


def run_even_game():
    run_game(get_question_and_answer, EVEN_INSTRUCTION)
