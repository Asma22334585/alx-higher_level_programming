#!/usr/bin/python3
def no_c(my_string):
    rmv = ""
    for x in range(len(my_string)):
        if (my_string[x] != 'c' and my_string[x] != 'C'):
            rmv += my_string[x]
    return rmv
