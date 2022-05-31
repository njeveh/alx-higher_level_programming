#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for character in str:
        character = ord(character)
        if character in range(97, 123):
            character -= 32
        print("{0:c}".format(character), end='')
