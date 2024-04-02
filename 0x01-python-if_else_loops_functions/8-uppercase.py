#!/usr/bin/python3
def uppercase(str):
    x = str
    for i in range(0, len(str)):
        if ord(str[i]) in range(97, 123):
            x = x[:i] + chr(ord(x[i]) - 32) + x[i+1:]
    print("{}".format(x))
