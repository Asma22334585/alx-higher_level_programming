#!/usr/bin/python3
"""matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by
    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float)
    Returns:
        new matrix
    Raises:
        TypeError: If matrix is not list of lists of integers/floats
        TypeError: If row haven't the same size.
        TypeError: If div is not a number
        ZeroDivisionError: If div equal to 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
