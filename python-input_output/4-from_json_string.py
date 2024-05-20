#!/usr/bin/python3
"""Defines a module"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    decoded = json.loads(my_str)
    return decoded
