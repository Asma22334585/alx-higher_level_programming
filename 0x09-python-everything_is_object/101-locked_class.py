#!/usr/bin/python3
"""defines LockedClass"""


class LockedClass:
     """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
