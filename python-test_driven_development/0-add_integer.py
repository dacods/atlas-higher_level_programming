#!/usr/bin/python3
"""Function that adds 2 integers"""


def add_integers(a, b=98):
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    
    return a + b
