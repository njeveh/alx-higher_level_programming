#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

if __name__ == "__main__":
    print("{0:d} + {0:d} = {0:d}".format(a, b, add(a, b)))
