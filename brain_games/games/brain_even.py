# coding=UTF-8

"""Logic module for brain game EVEN"""

from random import randint

from brain_games import cli
from brain_games.games import settings


def start():
    """Logics module for brain even game."""
    cli.welcome_message('Answer "yes" if number even otherwise answer "no".\n')
    username = cli.get_username_and_hello()
    for _ in range(settings.COUNT_OF_QUESTIONS):
        rand_number = randint(settings.MIN_RAND_NUM, settings.MAX_RAND_NUM)
        correct_answer = ['yes', 'no'][rand_number % 2]
        cli.print_question_phrase(rand_number)
        user_answer = cli.get_answer()
        if user_answer == correct_answer:
            cli.print_correct_phrase()
        else:
            cli.print_wrong_phrase(user_answer, correct_answer, username)
            return
    cli.print_congrats_phrase(username)
