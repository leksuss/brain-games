# coding=UTF-8

"""Logics module for brain games."""

from random import randint

from brain_games import cli

MIN_RAND_NUMBER = 1
MAX_RAND_NUMBER = 10e6
COUNT_OF_QUESTIONS = 3


def brain_even_start():
    """Logics module for brain even game."""
    name = cli.welcome_user(
        'Answer "yes" if number even otherwise answer "no".\n',
    )
    for _ in range(COUNT_OF_QUESTIONS):
        rand_number = randint(MIN_RAND_NUMBER, MAX_RAND_NUMBER)
        correct_answer = ['yes', 'no'][rand_number % 2]
        cli.print_response('Question: {0}'.format(rand_number))
        answer = cli.get_answer('Your answer: ')
        if answer == correct_answer:
            cli.print_response('Correct!')
        else:
            cli.print_response(
                '"{0}" is wrong answer ;(. Correct answer was "{1}".'.format(
                    answer,
                    correct_answer,
                ))
            cli.print_response("Let's try again, {0}!".format(name))
            return
    cli.print_response('Congratulations, {0}!'.format(name))
