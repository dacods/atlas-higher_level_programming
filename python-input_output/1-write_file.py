#!/usr/bin/python3
"""Defines a module"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file and
    returns the number of characters written"""
    with open(filename, 'w') as text:
        text.write("{}".format(text))
