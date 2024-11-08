#!/usr/bin/env python3

from brain_games.engine.engine import procedure
from brain_games.games.prime import prime
from brain_games.consts import q_prime


def main():
    procedure(prime, q_prime)


if __name__ == '__main__':
    main()
