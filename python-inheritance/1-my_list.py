#!/usr/bin/python3
"""Define a module"""


class Mylist(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
