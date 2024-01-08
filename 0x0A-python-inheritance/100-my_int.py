#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """ inherits from int"""
     def __init__(self, numbr):
        """Initializes MyInt
        Args:
            numbr: int
        """

        self.numbr = numbr

    def __eq__(self, value):
        """Inverts == to !="""
        return int(self) != value

    def __ne__(self, value):
        """Inverts != to =="""
        return int(self) == value
