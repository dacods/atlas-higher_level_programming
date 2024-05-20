#!/usr/bin/python3
""" Define a module """


class MyList(list):
    """ Defines a class """
    def print_sorted(self):
        """ Prints a sorted list """
        sorted_list = sorted(self)
        print(sorted_list)
