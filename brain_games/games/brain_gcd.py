# coding=UTF-8

"""Module for brain game GCD."""

from brain_games.games import engine


def get_gcd(num1, num2):
    """Calculate GCD for 2 numbers.

    Args:
        num1: first number
        num2: second number

    Returns:
        GCD for 2 numbers
    """
    return get_gcd(abs(num2), num1 % num2) if num2 else num1


def prepare_condition_for_one_game():
    """Get condition and answer for the game.

    Returns:
        tuple of two values:
            str with phrase user asked
            int right answer which user should write
    """
    num1, num2 = engine.get_rand_num(), engine.get_rand_num()
    return '{0} {1}'.format(num1, num2), get_gcd(num1, num2)


def start():
    """Run common logic for calc game."""
    engine.run_common_logic(
        'Find the greatest common divisor of given numbers.',
        prepare_condition_for_one_game,
    )
