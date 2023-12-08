#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    totalScore = 0
    totalWeight = 0

    for score, weight in my_list:
        totalScore += score * weight
        totalWeight += weight
    return totalScore / totalWeight
