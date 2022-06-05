#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order."""
    rev_list = my_list.reverse()
    for i in rev_list:
        print("{:d}".format(i))
