#!/usr/bin/python3

"""
This module prints a text with 2 new lines after . ? and :
"""


def text_indentation(text):
    """
    prints a text
    args:
        text(string): String to be printed
        no space at the beginning or end of each printed line
    Raises:
        TypeError: If text is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(f"{text}", end="")
