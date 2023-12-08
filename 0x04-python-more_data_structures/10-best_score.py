#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = 0
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                best_key = key
        return best_key
    return None
