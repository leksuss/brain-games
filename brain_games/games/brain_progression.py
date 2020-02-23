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
    start_progr = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    step_progr = random.randint(MIN_PROGR_STEP, MAX_PROGR_STEP)
    progression = [start_progr + step_progr * elem for elem in range(10)]
    rand_index = random.randint(0, PROGR_LENGTH - 1)
    correct_answer = progression[rand_index]
    progression[rand_index] = '…'
    return ' '.join(str(elem) for elem in progression), str(correct_answer)
