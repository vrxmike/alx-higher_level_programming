#!/usr/bin/python3

"""a function that prints all integers of a list, in reverse order."""

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for integer in reversed(my_list):
            print("{:d}".format(integer))
