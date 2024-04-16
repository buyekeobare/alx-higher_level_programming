#!/usr/bin/python3
"""This module is 4-from_json_string.py"""


import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string."""
    return json.loads(my_str)
