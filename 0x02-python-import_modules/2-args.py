#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("{:s}".format("1 argument:"))
    else:
        if argc > 0:
            print("{:d} arguments:".format(argc))
        else:
            print("0 arguments.")

    for i in range(argc):
        print("{:d}: {:s}".format(i, argv[i]))
