# coding=UTF-8

"""Logic engine for all games."""

import random

from brain_games import cli

MIN_RAND_NUM = 1
MAX_RAND_NUM = 50
COUNT_OF_QUESTIONS = 3


def get_rand_num(min_num=MIN_RAND_NUM, max_num=MAX_RAND_NUM):
    """Return random int number N, min_num <= N <= max_num.

    Args:
        min_num: min rand num, int
        max_num: max rand num, int

    Returns:
        random int number
    """
    return random.randint(min_num, max_num)


def run_common_logic(game_rules, condition_func):
    """Logics module for all games.

    Args:
        game_rules: str phrase with game rules
        condition_func: function prepearing conditions for the game
    """
    cli.welcome_message('{0}\n'.format(game_rules))
    username = cli.get_username_and_hello()
    for _ in range(COUNT_OF_QUESTIONS):
        question_phrase, correct_answer = condition_func()
        cli.print_question_phrase(question_phrase)
        user_answer = cli.get_answer()
        if user_answer == str(correct_answer):
            cli.print_correct_phrase()
        else:
            cli.print_wrong_phrase(user_answer, correct_answer, username)
            return
    cli.print_congrats_phrase(username)
