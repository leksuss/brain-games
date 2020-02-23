# coding=UTF-8

"""Module for brain game CALC."""

import operator
import random

MIN_RAND_NUM = 1
MAX_RAND_NUM = 50
RULES = 'What is the result of the expression?'
OPERATIONS = (
    ('*', operator.mul),
    ('+', operator.add),
    ('-', operator.sub),
)


def run() -> tuple:
    """Return condition and right answer of the game."""
    rand_operation = random.choice(OPERATIONS)
    num1 = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    num2 = random.randint(MIN_RAND_NUM, MAX_RAND_NUM)
    question_phrase = '{0} {2} {1}'.format(num1, num2, rand_operation[0])
    return question_phrase, str(rand_operation[1](num1, num2))
