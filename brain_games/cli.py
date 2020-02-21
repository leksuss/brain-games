# coding=UTF-8

"""Command line module."""

import prompt


def welcome_message(description=''):
    """Welcome message with game description.

    Args:
        description: The game rules and/or description.
    """
    print('Welcome to the Brain Games!', description, sep='\n')
    print()


def welcome_player():
    """Ask user to tell his name and say hello.

    Returns:
        name of user
    """
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))
    return username


def get_answer(prompt_phrase='Your answer: '):
    """Retrive answer from user.

    Args:
        prompt_phrase: The phrase shown user as a question.

    Returns:
        user's answer
    """
    return prompt.string(prompt_phrase)


def ask_question(phrase):
    """Print question phrase to user.

    Args:
        phrase: question phrase/equation
    """
    print('Question: {0}'.format(phrase))


def inform_wrong(user_answer, correct_answer, username):
    """Print wrong phrase to user.

    Args:
        user_answer: answer given by user
        correct_answer: correct answer
        username: name of user
    """
    print('"{0}" is wrong answer ;(. Correct answer was "{1}".'.format(
        user_answer,
        correct_answer,
    ))
    print("Let's try again, {0}!".format(username))


def inform_right():
    """Print correct phrase to user."""
    print('Correct!')


def congratulate(username):
    """Print congratulation phrase to user.

    Args:
        username: The name of user we want to congrats.
    """
    print('Congratulations, {0}!'.format(username))
