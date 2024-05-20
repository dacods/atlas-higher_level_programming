#!/usr/bin/python3
"""Deines a module"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    data = json.dumps(my_obj, indent=4)
    return data