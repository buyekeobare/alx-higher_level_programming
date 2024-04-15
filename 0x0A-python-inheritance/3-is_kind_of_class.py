#!/usr/bin/python3
"""This module is 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of a class
    or a class that the class in question inherits from.
    """
    return (isinstance(obj, a_class))
