#!/usr/bin/python3
"""This module is 6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file."""
    with open(filename) as f:
        return json.load(f)
