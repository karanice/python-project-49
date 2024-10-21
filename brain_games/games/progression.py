from random import randint
from random import choice


def print_progression():
    print('What number is missing in the progression?')


def gen_and_check():
    rules = ['1', '2', '3', '4', '5']
    rule = choice(rules)

    start_number = randint(2, 9)

    progression = [str(start_number)]
    el = start_number

    for i in range(1, 10):
        match rule:
            case '1':
                el = el + 2
            case '2':
                el = el + 3
            case '3':
                el = el - 4
            case '4':
                el = el + 5
            case '5':
                el = el + 7

        progression.append(str(el))
        i += 1

    index_to_replace = randint(0, 9)
    check = progression[index_to_replace]
    progression[index_to_replace] = '..'

    progression_to_show = ' '.join(progression)

    print(f'Question: {progression_to_show}')

    return check
