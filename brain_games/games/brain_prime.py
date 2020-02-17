# coding=UTF-8

"""Module for brain game Progression."""

import math

from brain_games.games import engine


def is_prime(number):
    """Check if given number is prime.

    Args:
        number: number to check

    Returns:
        Boolean result of check, True or False
    """
    for divider in range(2, math.ceil(number**0.5)):
        if not number % divider:
            return False
    return True


def prepare_condition_for_one_game():
    """Get condition and answer for the game.

    Returns:
        tuple of two values:
            int with phrase user asked
            str right answer which user should write
    """
    rand_num = engine.get_rand_num()
    return rand_num, ['no', 'yes'][is_prime(rand_num)]


def start():
    """Run common logic for calc game."""
    engine.run_common_logic(
        'Answer "yes" if given number is prime. Otherwise answer "no"',
        prepare_condition_for_one_game,
    )
