#!/usr/bin/python3

"""
This module contains a function that prints the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints ``My name is <first name> <last name>``.
    Args:
        first_name(string): First name to be printed
        last_name(string): Second name to be printed
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
