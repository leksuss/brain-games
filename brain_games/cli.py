# coding=UTF-8

"""Command line module."""

import prompt


def welcome_user():
    """Welcome message and get user name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
