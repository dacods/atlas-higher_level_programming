#!/usr/bin/python3
"""deines a module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    data = {"{}".format(filename)}

    x = json.loads(data)

    return x
