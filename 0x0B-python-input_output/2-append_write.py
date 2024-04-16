#!/usr/bin/python3
"""This module is 2-append_write.py"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
