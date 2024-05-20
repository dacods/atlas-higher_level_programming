#!/usr/bin/python3
"""Defines a module"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        value = {my_obj}

        return json.dumps(value)
