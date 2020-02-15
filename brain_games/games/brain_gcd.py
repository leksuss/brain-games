# coding=UTF-8

"""Logic module for brain game GCD."""

import random

from brain_games import cli
from brain_games.games import settings


def get_gcd(num1, num2):
    return get_gcd(abs(num2), num1 % num2) if num2 else num1


def start():
    """Logics module for brain even game."""
    cli.welcome_message('Find the greatest common divisor of given numbers.\n')
    username = cli.get_username_and_hello()

    for _ in range(settings.COUNT_OF_QUESTIONS):
        num1 = random.randint(settings.MIN_RAND_NUM, settings.MAX_RAND_NUM)
        num2 = random.randint(settings.MIN_RAND_NUM, settings.MAX_RAND_NUM)
        correct_answer = get_gcd(num1, num2)
        cli.print_question_phrase('{0} {1}'.format(num1, num2))
        user_answer = cli.get_answer()
        if user_answer == str(correct_answer):
            cli.print_correct_phrase()
        else:
            cli.print_wrong_phrase(user_answer, correct_answer, username)
            return
    cli.print_congrats_phrase(username)
