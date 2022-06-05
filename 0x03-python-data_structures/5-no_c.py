#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string."""
    if my_string:
        new_string = my_string[:]
        new_string.remove(i for i in new_string if i == 'c' or i == 'C')
        return str(new_string)
