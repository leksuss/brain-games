# coding=UTF-8

"""Logic module for brain game Progression."""

import math
import random

from brain_games import cli
from brain_games.games import settings


def is_prime(number):
    """Check if given number is prime.

    Args:
        number: number to check

    Returns:
        Boolean result of check, True or False
    """
    for divider in range(2, math.ceil(number**0.5)):
        if not number % divider:
            return False
    return True


def start():
    """Logics module for brain progression game."""
    cli.welcome_message(
        'Answer "yes" if given number is prime. Otherwise answer "no".\n',
    )
    username = cli.get_username_and_hello()
    for _ in range(settings.COUNT_OF_QUESTIONS):
        rand_num = random.randint(settings.MIN_RAND_NUM, settings.MAX_RAND_NUM)
        correct_answer = ['no', 'yes'][is_prime(rand_num)]
        cli.print_question_phrase(rand_num)
        user_answer = cli.get_answer()
        if user_answer == str(correct_answer):
            cli.print_correct_phrase()
        else:
            cli.print_wrong_phrase(user_answer, correct_answer, username)
            return
    cli.print_congrats_phrase(username)
