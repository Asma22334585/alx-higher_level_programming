#!/usr/bin/python3
"""pascal_triangle fnct"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        x = tri[-1]
        tmp = [1]
        for i in range(len(x) - 1):
            tmp.append(x[i] + x[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
