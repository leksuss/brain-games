# coding=UTF-8

"""Brain Prograssion Game module."""

from brain_games import engine
from brain_games.games import brain_progression


def main():
    """Run game engine for brain_progression game."""
    engine.run(brain_progression)


if __name__ == '__main__':
    main()
