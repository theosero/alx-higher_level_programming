#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arg = len(sys.argv) - 1
    total = 0
    for i in range(arg):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
