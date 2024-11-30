import math
from brain_games.engine.engine import run_game
from brain_games.consts import GCD_INSTRUCTION
from brain_games.utils import get_random_number


def get_nums_pair_and_gcd():
    first_num, second_num = get_random_number(), get_random_number()
    nums_pair = f'{first_num} {second_num}'
    gcd = math.gcd(first_num, second_num)

    return nums_pair, gcd


def run_gcd_game():
    run_game(get_nums_pair_and_gcd, GCD_INSTRUCTION)
