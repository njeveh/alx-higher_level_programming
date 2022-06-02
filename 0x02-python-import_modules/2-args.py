#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    if argc == 1:
        print("{:d} arguments.".format(argc - 1))
    elif argc == 2:
        print("{:d} argument:".format(argc - 1))
    else:
        print("{:d} arguments:".format(argc - 1))

    for i, arg in enumerate(argv[1:], 1):
        print("{:d}: {}".format(i, arg))
