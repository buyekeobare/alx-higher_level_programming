#!/usr/bin/python3
"""This is class to JSON module"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
