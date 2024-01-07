#!/usr/bin/python3
"""matrix_mul method."""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices.
    Args:
        m_a: matrix 1
        m_b: matrix 2
    Returns:
        matrix: mul
    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty.
        TypeError: If element is not an integer or a float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnumbr = False
    m_b_notnumbr = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnumbr = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnumbr = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnumbr:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notnumbr:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_notrect:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_notrect:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    x = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            w = 0
            for k in range(len(m_b)):
                w += m_a[i][k] * m_b[k][j]
            x[i].append(w)

    return x

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
