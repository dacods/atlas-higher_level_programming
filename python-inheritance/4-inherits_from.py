#!/usr/bin/python3
"""Defines a module"""


def inherits_from(obj, a_class):
    """Return true if object is an instace
    of a class inherited from specified
    class otherwise false"""
    return isinstance(obj, a_class) and type(obj) is not a_class
