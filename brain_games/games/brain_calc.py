# coding=UTF-8

"""Module for brain game CALC."""

import random

from brain_games.games import engine


def prepare_condition_for_one_game():
    """Get condition and answer for the game.

    Returns:
        tuple of two values:
            str with phrase user asked
            str right answer which user should write
    """
    operations = {
        '*': lambda num1, num2: num1 * num2,
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2,
    }
    rand_operation = random.choice(list(operations.keys()))
    num1, num2 = engine.get_rand_num(), engine.get_rand_num()
    correct_answer = operations[rand_operation](num1, num2)
    question_phrase = '{0} {2} {1}'.format(num1, num2, rand_operation)
    return question_phrase, correct_answer


def start():
    """Run common logic for calc game."""
    engine.run_common_logic(
        'What is the result of the expression?',
        prepare_condition_for_one_game,
    )
