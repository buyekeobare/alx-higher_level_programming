#!/usr/bin/python3
"""Defines a locked class with no class or object attribute."""


class LockedClass:
    """
    Prevent the user from instantiating new locked class attributes
    for anything other than attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
