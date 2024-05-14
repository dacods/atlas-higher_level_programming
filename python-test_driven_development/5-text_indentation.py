#!/usr/bin/python3
"""Function that prints a text with 2 new lines"""


def text_indentation(text):
    """Prints new lines after ., /, and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = []
    line = ''

    for char in text:
        line += char
        if char in punctuations:
            lines.append(line.strip())
            lines.append('')
            line = ''

    if line:
        lines.append(line.strip())

    for line in lines:
        print({}.format(line))
