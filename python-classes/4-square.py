#!/usr/bin/python3
"""Defines a class"""


class Sqaure:
    """Defines a Square"""

    def __init__(self, size=0):
        self.__size - size

    def size(self):
        return self.size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
