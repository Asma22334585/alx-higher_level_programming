#!/usr/bin/python3
"""defines LockedClass"""

class LockedClass:
    """except if the new instance attribute is called first_name"""

     __slots__ = ['first_name']
