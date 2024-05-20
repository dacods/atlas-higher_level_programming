#!/usr/bin/python3
"""Defines a module"""


def append_write(filename="", text=""):
    """Appends a string at the end of text file and
    returns the number of characters"""
    with open(filename, 'a') as file:
        file.write(text)
