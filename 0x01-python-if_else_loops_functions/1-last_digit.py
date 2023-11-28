#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
m = number % 10 if number > 10 else number % -10
print("Last digit of {} is {} and is".format(number, m), end="")
if m > 5:
    print("greater than 5")
elif m == 0:
    print("0")
elif m < 6:
    print("less than 6 and not 0")
