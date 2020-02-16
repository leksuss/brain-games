# coding=UTF-8

"""Logic module for brain game Progression."""

import random

from brain_games import cli
from brain_games.games import settings

PROGRESSION_LENGTH = 10
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10


def get_progression(curr_num=None, step=None, progression=None):
    """Generate arithmetical progression with skipped number.

    Args:
        curr_num: current number of arithmetical progression as int
        step: step of arithmetical progression as int
        progression: progression as list

    Returns:
        Tuple of two values:
            Arithmetical progression with skipped number as string
            Secret number of progression which should be guessed as int
    """
    if progression is None:
        progression = []
        curr_num = random.randint(settings.MIN_RAND_NUM, settings.MAX_RAND_NUM)
        step = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    if len(progression) < PROGRESSION_LENGTH:
        progression.append(str(curr_num))
        return (get_progression(curr_num + step, step, progression))
    rand_index = random.randint(0, 9)
    secret_num = progression[rand_index]
    progression[rand_index] = '…'
    return ' '.join(progression), secret_num


def start():
    """Logics module for brain progression game."""
    cli.welcome_message('What number is missing in the progression?\n')
    username = cli.get_username_and_hello()
    for _ in range(settings.COUNT_OF_QUESTIONS):
        progression, correct_answer = get_progression()
        cli.print_question_phrase(progression)
        user_answer = cli.get_answer()
        if user_answer == str(correct_answer):
            cli.print_correct_phrase()
        else:
            cli.print_wrong_phrase(user_answer, correct_answer, username)
            return
    cli.print_congrats_phrase(username)
