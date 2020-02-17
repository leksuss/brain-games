# coding=UTF-8

"""Module for brain game Progression."""

from brain_games.games import engine

PROGR_LENGTH = 10
MIN_PROGR_STEP = 1
MAX_PROGR_STEP = 10


def prepare_condition_for_one_game():
    """Get condition and answer for the game.

    Returns:
        tuple of two values:
            str with phrase user asked
            int right answer which user should write
    """
    progression = [str(engine.get_rand_num())]
    step_progr = engine.get_rand_num(MIN_PROGR_STEP, MAX_PROGR_STEP)
    for _ in range(PROGR_LENGTH):
        progression.append(str(int(progression[-1]) + step_progr))
    rand_index = engine.get_rand_num(0, PROGR_LENGTH)
    correct_answer = progression[rand_index]
    progression[rand_index] = '…'
    return ' '.join(progression), correct_answer


def start():
    """Run common logic for calc game."""
    engine.run_common_logic(
        'What number is missing in the progression?',
        prepare_condition_for_one_game,
    )
