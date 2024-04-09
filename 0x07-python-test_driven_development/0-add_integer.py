#!/usr/bin/python3

"""
This module adds two integers

"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers a and b
    Args:
        a(int, float) first argument
        b(int, float) second argument
    Returns:
        sum of a and b
    Raises:
        TypeError: If either a or b is not an integer or a float

    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (int(a) + int(b))
