#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list(my_list)

    if idx < 0 or idx >= len(my_list):
        return list(my_list)

    new_list = list(my_list)
    new_list[idx] = element
    return (new_list)
