#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy = []

    for num in my_list:
        copy.append(num % 2 == 0)
    return copy
