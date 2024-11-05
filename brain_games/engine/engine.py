from brain_games.scripts.brain_games import greeting
from sys import exit
from prompt import string
from brain_games.games.calc import check as check_calc
from brain_games.games.even import gen_and_check as gac_even
from brain_games.games.gcd import gen_and_check as gac_gcd
from brain_games.games.prime import gen_and_check as gac_prime
from brain_games.games.progression import gen_and_check as gac_progression
from brain_games.rules.rules import p_calc
from brain_games.rules.rules import p_even
from brain_games.rules.rules import p_gcd
from brain_games.rules.rules import p_prime
from brain_games.rules.rules import p_progression


def get_name():
    name = string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def get_answer():
    answer = string('Your answer: ')
    return answer


def farewell(user_answer, check, user_name):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{check}'")
    print(f'Let\'s try again, {user_name}!')


def congrats(user_name):
    print(f'Congratulations, {user_name}!')


def procedure(trigger):
    greeting()
    user_name = get_name()

    match trigger:
        case 'calc':
            p_calc()
        case 'even':
            p_even()
        case 'gcd':
            p_gcd()
        case 'prime':
            p_prime()
        case 'progression':
            p_progression()

    i = 0
    for i in range(0, 3):
        match trigger:
            case 'calc':
                check = check_calc()
            case 'even':
                check = gac_even()
            case 'gcd':
                check = gac_gcd()
            case 'prime':
                check = gac_prime()
            case 'progression':
                check = gac_progression()

        user_answer = get_answer()

        if user_answer == check:
            i += 1
            print('Correct!')
        else:
            farewell(user_answer, check, user_name)
            exit()

    congrats(user_name)
