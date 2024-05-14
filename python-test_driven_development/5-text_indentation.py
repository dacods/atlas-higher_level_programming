#!/usr/bin/python3
"""Function that prints a text with 2 new lines"""


def text_indentation(text):
    """Prints new lines after ., /, and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    empty_str = ""

    for char in text:
        empty_str += char
        if char in punctuations:
            print(empty_str.strip())
            print()
            empty_str = ""
    if empty_str.strip():
        print(empty_str.strip(), end="")
