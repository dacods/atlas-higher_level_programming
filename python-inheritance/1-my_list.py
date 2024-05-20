#!/usr/bin/python3
"""Define a class"""


class Mylist(list):
    """Class that inherits from list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
