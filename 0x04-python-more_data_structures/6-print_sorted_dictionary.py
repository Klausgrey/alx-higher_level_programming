#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    numKeys = sorted(a_dictionary)
    for i in numKeys:
        print(f"{i}: {a_dictionary[i]}")
