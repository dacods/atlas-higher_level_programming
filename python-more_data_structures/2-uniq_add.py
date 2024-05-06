#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    total = 0

    for num in my_list:
        if num not in uniq:
            uniq.add(num)
            total += num

    return total