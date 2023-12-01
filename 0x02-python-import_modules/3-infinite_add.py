#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = 0
    for x in argv[1:]:
        i += int(x)
    print(i)
