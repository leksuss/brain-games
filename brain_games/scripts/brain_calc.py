# coding=UTF-8

"""Brain Calc Game module."""

from brain_games import engine
from brain_games.games import brain_calc


def main():
    """Run game engine for brain_calc game."""
    engine.run(brain_calc)


if __name__ == '__main__':
    main()
