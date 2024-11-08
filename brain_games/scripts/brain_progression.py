#!/usr/bin/env python3

from brain_games.engine.engine import procedure
from brain_games.games.progression import progression
from brain_games.consts import q_progression


def main():
    procedure(progression, q_progression)


if __name__ == '__main__':
    main()
