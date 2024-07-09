#!/usr/bin/python3
"""Module that contains a function that finds peak of an array"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers: a list of unsorted integers
    """

    length = len(list_of_integers)

    # handle the base case
    if length is None:
        return None
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    mid = int(length / 2)
    p = list_of_integers[mid]

    if p > list_of_integers[mid - 1] and p > list_of_integers[mid + 1]:
        return p
    elif p < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
