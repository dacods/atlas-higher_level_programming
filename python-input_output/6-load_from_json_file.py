#!/usr/bin/python3
"""deines a module"""
import json


def load_from_json_file(filename):
    data = {"{}".format(filename)}

    x = json.loads(data)

    return x