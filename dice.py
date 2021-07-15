"""Defines dice roll functions used in games."""

from random import randint

def roll_dice(amount, sides) -> int:
    """
    Rolls an amount of dice with sides number of faces, with the faces
    being numbered from 1 to sides.

    :return int: The result of the dice roll.
    """
    total = 0

    for i in range(amount):
        total += randint(1, sides)
    return total
