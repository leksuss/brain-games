# coding=UTF-8

"""Module for brain game Progression."""

import random

MIN_RAND_NUM = 1
MAX_RAND_NUM = 50
PROGR_LENGTH = 10
MIN_PROGR_STEP = 1
MAX_PROGR_STEP = 10
RULES = 'What number is missing in the progression?'


def run() -> tuple:
    """Get condition and answer for the game."""
    progression = [random.randint(MIN_RAND_NUM, MAX_RAND_NUM)]
    step_progr = random.randint(MIN_PROGR_STEP, MAX_PROGR_STEP)
    for _ in range(PROGR_LENGTH):
        progression.append(progression[-1] + step_progr)
    rand_index = random.randint(0, PROGR_LENGTH)
    correct_answer = progression[rand_index]
    progression[rand_index] = '…'
    return ' '.join(str(elem) for elem in progression), str(correct_answer)
