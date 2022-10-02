#!/usr/bin/python3

"""a function that deletes keys with
a specific value in a dictionary."""


def complex_delete(a_dictinary, value):
    while value in a_dictionary.values():
        for key, values in a_dictionary.items():
            if values == value:
                a_dictionary.pop(key, None)
                break
    return a_dictionary
