#!/usr/bin/python3
"""Defines a module"""


class Student:
    """Defines a class"""
    def __init__(self, firt_name, last_name, age):
        self.first_name = firt_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
