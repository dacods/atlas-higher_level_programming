#!/usr/bin/python3
"""deines a module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    try:
        with open(filename, mode='x') as file:
            file.write(file)
    except FileExistsError:
        pass
