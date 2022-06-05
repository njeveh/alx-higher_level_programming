#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list.
    """
    if my_list:
        boolean_list = [i % 2 == 0 for i in my_list]
        return boolean_list
