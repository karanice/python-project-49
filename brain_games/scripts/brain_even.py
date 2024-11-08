#!/usr/bin/env python3

from brain_games.engine.engine import procedure
from brain_games.games.even import even
from brain_games.consts import q_even


def main():
    procedure(even, q_even)


if __name__ == '__main__':
    main()
