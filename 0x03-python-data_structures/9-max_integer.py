#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list."""
    if my_list:
        return (my_list.sort()[0])
    else:
        return None
