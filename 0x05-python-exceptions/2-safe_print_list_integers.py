#!/usr/bin/python3

"""a function that prints the first x
elements of a list and only integers."""


def safe_print_list_integrs(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end='')
            count += 1
        except (ValueError, TypeError):
            countinue
    print('')
    return count
