#!/usr/bin/python3
"""
Addition module:
    Adding two integers.
    Raise exception if not integer.
    cast float into integer.
"""


def add_integer(a, b=98):
    """
    Function to add two int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a + b)
