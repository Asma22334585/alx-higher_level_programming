#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for sm in matrix:
        if len(sm) == 0:
            print()
        for x in range(len(sm)):
            print("{:d}".format(sm[x]),
                  end="\n" if x is len(sm) - 1 else " ")
