#!/usr/bin/env python3

from brain_games.engine.engine import procedure
from brain_games.games.gcd import gcd
from brain_games.consts import q_gcd


def main():
    procedure(gcd, q_gcd)


if __name__ == '__main__':
    main()
