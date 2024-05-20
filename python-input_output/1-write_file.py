#!/usr/bin/python3
"""Defines a module"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file and
    returns the number of characters written"""
    count = 0
    with open(filename) as f:
        for line in f:
            for char in line:
                if char in text:
                    count += 1
    return count
