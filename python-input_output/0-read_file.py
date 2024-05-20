#!/usr/bin/python3
"""Defines a module"""


def read_file(filename=""):
    """Function that reads a text file and prints to stdout"""
    with open(filename, 'r') as fin:
        print(fin.read(), end="")
