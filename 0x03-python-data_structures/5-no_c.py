#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for i in my_string:
        if i not in "cC":
            newStr += i
    return newStr
