#!/usr/bin/python3

import sys

if __name__ == '__main__':

    arg = len(sys.argv)

    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:")

    for i in range(arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
