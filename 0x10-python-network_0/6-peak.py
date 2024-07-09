#!/usr/bin/python3
"""Module that contains a function that finds peak of an array"""


def find_peak(list_of_integers):
    """Finds peak
    Args:
        list_of_integers (list): list of integers
    """
    len_lst = len(list_of_integers)
    if len_lst is None:
        return None
    peak = float('-inf')  # Initialize peak as negative infinity
    for num in list_of_integers:
        if num > peak:
            peak = num

    return peak
