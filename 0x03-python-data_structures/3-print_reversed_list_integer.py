#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """To print all integers of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for b in my_list:
            print("{:d}".format(b))
