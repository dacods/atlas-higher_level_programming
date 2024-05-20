#!/usr/bin/python3
"""Defines a module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
