#!/usr/bin/python3
"""prevents dynamically creating attributes"""


class LockedClass:
    """
    except if the new instance attribute is called first_name
    """
     __slots__ = ['first_name']
