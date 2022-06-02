#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv)
    if argc == 2:
        print("{:s}".format("1 argument:"))
    else:
        if argc > 2:
            print("{:d} arguments:".format(argc - 1))
        else:
            print("0 arguments.")

    for i in range(1, argc):
        print("{:d}: {:s}".format(i, argv[i]))
