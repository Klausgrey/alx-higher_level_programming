#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    for keys, i in a_dictionary.items():
        newDict[keys] = i * 2
    return newDict
