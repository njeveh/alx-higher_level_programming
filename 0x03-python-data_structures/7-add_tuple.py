#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples"""
    while len(tuple_a) < 2:
        tuple_a += 0,
    while len(tuple_b) < 2:
        tuple_b += 0,
    combined_tuple = zip(tuple_a, tuple_b)
    my_tuple = ()
    for tuple_x in combined_tuple:
        my_tuple += tuple_x[0] + tuple_x[1],
    return my_tuple
