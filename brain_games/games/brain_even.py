# coding=UTF-8

"""Module for brain game EVEN."""

from brain_games.games import engine


def prepare_condition_for_one_game():
    """Get condition and answer for the game.

    Returns:
        tuple of two values:
            str with phrase user asked
            str right answer which user should write
    """
    rand_num = engine.get_rand_num()
    return rand_num, ['yes', 'no'][rand_num % 2]


def start():
    """Run common logic for calc game."""
    engine.run_common_logic(
        'Answer "yes" if number even otherwise answer "no".',
        prepare_condition_for_one_game,
    )
