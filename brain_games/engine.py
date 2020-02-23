# coding=UTF-8

"""Logic engine for all games."""

from brain_games import cli

COUNT_OF_QUESTIONS = 3


def run(game):
    """Logic module for all games.

    Args:
        game: game module with game conditions and ruels
    """
    cli.welcome_message(game.RULES)
    username = cli.welcome_player()
    for _ in range(COUNT_OF_QUESTIONS):
        phrase, correct_answer = game.run()
        cli.ask_question(phrase)
        user_answer = cli.get_answer()
        if user_answer != correct_answer:
            cli.inform_wrong(user_answer, correct_answer, username)
            break
        cli.inform_right()
    else:
        cli.congratulate(username)
