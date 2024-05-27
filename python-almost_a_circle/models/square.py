#!/usr/bin/python3
"""Defines a module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}")