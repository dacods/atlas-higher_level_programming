#!/usr/bin/python3
"""Defines a module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
