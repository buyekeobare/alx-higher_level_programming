#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """To find all multiples of 2 in a list."""
    multiples = []
    for b in range(len(my_list)):
        if my_list[b] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
