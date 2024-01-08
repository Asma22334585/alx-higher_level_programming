#!/usr/bin/python3
"""adds attributes to objects"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if it’s possible
        Args:
            name : string
            value : value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
