#!/usr/bin/python3

"""a function that returns a tuple with the length of a string and its first character."""



def multiple_retutns(sentence):
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
