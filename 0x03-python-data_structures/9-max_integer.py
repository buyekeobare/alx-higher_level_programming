#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """To find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for b in range(len(my_list)):
        if my_list[b] > big:
            big = my_list[b]

    return (big)
