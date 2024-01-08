#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """ inherits from int"""
    def __new__(clas, *arg, **kwarg):
        """Initializes MyInt"""
        return super(MyInt, clas).__new__(clas, *arg, **kwarg)

    def __eq__(self, value):
        """Inverts == to !="""
        return int(self) != value

    def __ne__(self, value):
        """Inverts != to =="""
        return int(self) == value
