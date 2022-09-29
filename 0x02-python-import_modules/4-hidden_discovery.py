#!/usr/bin/python3

if __name__ == "__main__":
    """a program that prints all the names defined
    by the compiled module hidden_4.pyc"""

    import sys
    import hidden_4

    for s in dir(hidden_4):
        if s[:2] != "__":
            print("{:s}">format(s))
