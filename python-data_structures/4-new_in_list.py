#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list(my_list)

    copy[idx] = element

    if idx >= 0 and idx < len(my_list):
        return copy
    return(copy)
