# coding=UTF-8

"""Logic engine for all games."""

from brain_games import cli

COUNT_OF_QUESTIONS = 3


def run(game_rules, condition_func):
    """Logics module for all games.

    Args:
        game_rules: str phrase with game rules
        condition_func: function prepearing conditions for the game
    """
    cli.welcome_message(game_rules)
    username = cli.get_username_and_hello()
    for _ in range(COUNT_OF_QUESTIONS):
        question_phrase, correct_answer = condition_func()
        cli.print_question_phrase(question_phrase)
        user_answer = cli.get_answer()
        if user_answer != correct_answer:
            cli.print_wrong_phrase(user_answer, correct_answer, username)
            break
        cli.print_correct_phrase()
    else:
        cli.print_congrats_phrase(username)
