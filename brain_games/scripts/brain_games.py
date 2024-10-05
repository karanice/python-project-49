#!/usr/bin/env python 3

from brain_games.cli import welcome_user


def greeting():
    print('Welcome to the Brain Games!')


def main():
    greeting()
    print(f'Hello, {welcome_user()}!')


if __name__ == '__main__':
    main()
