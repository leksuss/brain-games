# coding=UTF-8

"""Module for brain game EVEN."""

import random

MIN_RAND_NUM = 1
MAX_RAND_NUM = 50
RULES = 'Answer "yes" if number even otherwise answer "no".'


def run() -> tuple:
    """Return condition and right answer of the game."""
    rand_num = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    return str(rand_num), 'no' if rand_num % 2 else 'yes'
