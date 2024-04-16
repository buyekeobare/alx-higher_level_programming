#!/usr/bin/python3
"""This module is 5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
