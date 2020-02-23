# coding=UTF-8

"""Module for brain game GCD."""

import random

MIN_RAND_NUM = 1
MAX_RAND_NUM = 50
RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1: int, num2: int) -> int:
    """Calculate GCD with num1 and num2."""
    return get_gcd(abs(num2), num1 % num2) if num2 else num1


def run() -> tuple:
    """Return condition and right answer of the game."""
    num1 = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    num2 = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    return '{0} {1}'.format(num1, num2), str(get_gcd(num1, num2))
