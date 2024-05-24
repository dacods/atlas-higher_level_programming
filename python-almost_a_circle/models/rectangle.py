#!/usr/bin/python3
"""Defines a module"""
Base = __import__('base.py').Base


class Rectangle(Base):
    """Definse a class"""
    def __init__(self, width, height, x, y):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width
