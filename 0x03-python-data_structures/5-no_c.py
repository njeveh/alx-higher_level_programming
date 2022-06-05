#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string."""
    new_s = my_string.translate({ord('c'): None})
    new_s = new_s.translate({ord('C'): None})
    return new_s
