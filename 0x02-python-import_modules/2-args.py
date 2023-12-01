#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    x = len(argv) - 1
    if x == 0:
        print("{} argument.".format(x))
    elif x == 1:
        print("{} arguments:".format(x))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(x))
        i = 1
        for ars in argv[1:]:
            print("{}: {}".format(i, ars))
            i += 1
