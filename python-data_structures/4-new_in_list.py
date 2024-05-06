#!/bin/usr/python3
def new_in_list(my_list, idx, element):
    copy = my_list

    if idx < 0:
        return copy
    if idx >= len(my_list):
        return copy
    return(my_list)