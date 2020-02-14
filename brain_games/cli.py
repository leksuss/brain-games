# coding=UTF-8

"""Command line module."""

import prompt


def welcome_user(description=''):
    """Welcome message with game description and getting username.

    Print welcome message and game rules and description, after that ask
    user name.

    Args:
        description: The game rules and it's description.

    Returns:
        name of user
    """
    print_response('Welcome to the Brain Games!')
    print_response(description)
    name = prompt.string('May I have your name? ')
    print_response('Hello, {0}!'.format(name))
    return name


def get_answer(prompt_phrase):
    """Retrive answer from user.

    Args:
        prompt_phrase: The phrase shown user as a question.

    Returns:
        user's answer
    """
    return prompt.string(prompt_phrase)


def print_response(phrase):
    """Print phrase to user.

    Args:
        phrase: The print phrase to user.
    """
    print(phrase)
