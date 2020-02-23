# coding=UTF-8

"""Brain Prime Game module."""

from brain_games import engine
from brain_games.games import brain_prime


def main():
    """Run game engine for brain_prime game."""
    engine.run(brain_prime)


if __name__ == '__main__':
    main()
