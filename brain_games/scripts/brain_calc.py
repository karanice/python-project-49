#!/usr/bin/env python3

from brain_games.engine.engine import procedure
from brain_games.games.calc import calc
from brain_games.consts import q_calc


def main():
    procedure(calc, q_calc)


if __name__ == '__main__':
    main()
