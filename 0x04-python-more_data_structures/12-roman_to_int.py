#!/usr/bin/python3
"""a function that converts a Roman numeral to an integer."""

def roman_to_int(roman_string):
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return number
    else:
        splitted = list(roman_string)
        sliced = [conv[i] for i in splitted]
        length = len(sliced)
        count = 0
        while count < length:
            if count != length-1:
                if sliced[count] < sliced[count+1]:
                    number += abs(sliced[count] - sliced[count+1])
                    count += 2
                else:
                    number += sliced[count]
                    count += 1
            else:
                number += sliced[count]
                count += 1
        return number
