#!/usr/bin/python3
"""deines a module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'w+') as file:
        x = json.loads(file)
    return x
