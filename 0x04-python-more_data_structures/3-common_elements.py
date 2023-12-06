#!/usr/bin/python3
def common_elements(set_1, set_2):
    valur_1 = set(set_1)
    valur_2 = set(set_2)
    common = valur_1.intersection(valur_2)
    return common
