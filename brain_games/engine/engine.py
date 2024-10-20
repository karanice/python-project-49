from brain_games.scripts.brain_games import greeting
from sys import exit
from brain_games.games.calc import gen_and_check as gac_calc
from brain_games.games.even import gen_and_check as gac_even
from brain_games.games.gcd import gen_and_check as gac_gcd
from brain_games.games.prime import gen_and_check as gac_prime
from brain_games.games.progression import gen_and_check as gac_progression
from brain_games.games.calc import print_calc
from brain_games.games.even import print_even
from brain_games.games.gcd import print_gcd
from brain_games.games.prime import print_prime
from brain_games.games.progression import print_progression


def get_name():
    name = ''
    while name == '':
        name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    answer = ''
    while answer == '':
        answer = input('Your answer: ')
    return answer


def procedure(trigger):
    greeting()
    user_name = get_name()
         
    match trigger:
        case 'calc':
            print_calc()
        case 'even':
            print_even()
        case 'gcd':
            print_gcd()
        case 'prime':
            print_prime()
        case 'progression':
            print_progression()

    i = 0
    while i != 3:
        match trigger:
            case 'calc':
                check = gac_calc()
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
            i = 0
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{check}'")
            print(f'Let\'s try again, {user_name}!')
            exit()

    print(f'Congratulations, {user_name}!')