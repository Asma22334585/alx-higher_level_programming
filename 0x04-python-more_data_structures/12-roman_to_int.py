#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance (roman_string, str):
        return 0
    s = 0
    n = 0
    digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    for y in reversed(roman_string):
        n = digit[y]
        s += n if s < n * 5 else -n
    return s
