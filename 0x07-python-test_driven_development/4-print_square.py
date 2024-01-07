#!/usr/bin/python3
"""print_square method"""


def print_square(size):
    """print a square with #.

    Args:
        size:  length of the square

    Raises:
        TypeError: If size not an int.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
