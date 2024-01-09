#!/usr/bin/python3
"""pascal_triangle fnct"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return []

    lenght = [[0 for x in range(i + 1)] for i in range(n)]
    lenght[0] = [1]

    for i in range(1, n):
        lenght[i][0] = 1
        for j in range(1, i + 1):
            if j < len(l[i - 1]):
                lenght[i][j] = lenght[i - 1][j - 1] + lenght[i - 1][j]
            else:
                lenght[i][j] = lenght[i - 1][0]
    return lenght
