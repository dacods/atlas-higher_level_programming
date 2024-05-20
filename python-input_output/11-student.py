#!/usr/bin/python3
"""Defines a module"""


class Student:
    """Defines a class"""
    def __init__(self, firt_name, last_name, age):
        self.first_name = firt_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = {}

        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
