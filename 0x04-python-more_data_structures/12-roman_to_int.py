#!/usr/bin/python3
def roman_to_int(roman_string):
    #checks if the arguments passed is [None] returns 0
    if roman_string is None:
        return 0
    #checks if the argument [passed] is not a string and return 0
    if not isinstance(roman_string, str):
        return 0
    romanValue = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    totalValue = 0
    previousValue = 0
    for i in roman_string:
        currentValue = romanValue[i]
        totalValue += currentValue
        if currentValue > previousValue:
            totalValue -= 2 * previousValue
        previousValue = currentValue
    return totalValue
