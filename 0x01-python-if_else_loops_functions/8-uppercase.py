#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = uppercase(i)
        print(x, end="")
        # if ord(i) >= 97 and ord(i) <= 122:
        #     x = chr(ord(i) - 32)
        # else:
        #     x = i
        #     print("{}".format(x), end="")
    print()