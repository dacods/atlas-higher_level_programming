#!/usr/bin/python3
"""Function that adds 2 integers"""


def add_integer(a, b=98):
    """Returns the added values or raises an Type Error"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
