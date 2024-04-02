#!/usr/bin/python3
"""add_integer method"""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: int 1
        b: int 2, default 98.

    Raises:
        TypeError: a and b must be integers or floats

    Returns:
        the addition of a and b
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError('a must be an integer')
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
