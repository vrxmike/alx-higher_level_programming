#!/usr/bin/python3

"""a function that returns the weighted
avarage of all integers tuple (<score>, <weight>)"""

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wa_sum = 0
    div = 0
    for score, weight in my_list:
        wa_sum += (score * weight)
        div += weight
    return wa_sum / div
