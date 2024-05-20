#!/usr/bin/python3
"""Defines a module"""


def is_same_class(obj, a_class):
    """Function that returns true if exactlay an instace otherwise flase"""
    if type(obj) is a_class:
        return True
    else:
        return False
