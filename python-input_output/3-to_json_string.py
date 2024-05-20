#!/usr/bin/python3
"""Deines a module"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    decoder = json.JSONDecoder()
    data = decoder.decode(my_obj)
    return data