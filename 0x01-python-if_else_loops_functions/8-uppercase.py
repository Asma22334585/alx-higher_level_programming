#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    newstr = ""
    for c in str:
        newstr += "%c" % islower(c)
    print("{:s}".format(newstr))
