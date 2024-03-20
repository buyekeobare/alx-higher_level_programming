#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for p in list_ord:
        print("{}: {}".format(p, a_dictionary.get(p)))
