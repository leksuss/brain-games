# coding=UTF-8

"""Module for brain game Progression."""

import math
import random

MIN_RAND_NUM = 1
MAX_RAND_NUM = 50
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(number: int) -> bool:
    """Check if given number is prime."""
    for divider in range(2, math.ceil(number**0.5)):
        if not number % divider:
            return False
    return True


def run() -> tuple:
    """Return condition and right answer of the game."""
    rand_num = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    return str(rand_num), 'yes' if is_prime(rand_num) else 'no'
