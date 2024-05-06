#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    val = None

    for key, value in a_dictionary.items():
        if value > num:
            num = value
            val = key
    return val
