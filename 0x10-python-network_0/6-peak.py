#!/usr/bin/python3
"""Finds the peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """
    Args:
    list_of_integers(int): list of integers to find peak
    Returns:
    integers(peak) or None
    """

    if not list_of_integers:
        return None

    l, h = 0, len(list_of_integers) - 1

    while l < h:
        middle = (l + h) // 2
        if list_of_integers[middle] > list_of_integers[middle + 1]:
            h = middle
        else:
            l = middle + 1
    return list_of_integers[l]
