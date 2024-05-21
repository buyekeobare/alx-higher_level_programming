#!/usr/bin/python3

"""
This module prints a square with the character #
"""


def print_square(size):
    """
    This function prints a square where size is the length of the square
    args:
        size(int) : Represeents the length of square
    Raises:
        TypeError: If size is not an int
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float or size < 0:
        raise TypeError("size must be an integer")

    for k in range(size):
        for l in range(size):
            print("#", end="")
        print()
