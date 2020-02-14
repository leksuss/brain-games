# coding=UTF-8

"""Logics module for brain games."""

import random

from brain_games import cli
from brain_games.games import settings


def start():
    """Logics module for brain even game."""
    cli.welcome_message('What is the result of the expression?\n')
    username = cli.get_username_and_hello()
    operations = {
        '*': lambda num1, num2: num1 * num2,
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2,
    }
    for _ in range(settings.COUNT_OF_QUESTIONS):
        num1 = random.randint(settings.MIN_RAND_NUM, settings.MAX_RAND_NUM)
        num2 = random.randint(settings.MIN_RAND_NUM, settings.MAX_RAND_NUM)
        operation = random.choice(list(operations.keys()))
        correct_answer = operations[operation](num1, num2)
        cli.print_question_phrase('{0} {2} {1}'.format(num1, num2, operation))
        user_answer = cli.get_answer()
        if user_answer == str(correct_answer):
            cli.print_correct_phrase()
        else:
            cli.print_wrong_phrase(user_answer, correct_answer, username)
            return
    cli.print_congrats_phrase(username)
