#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """writes a string to a text file
    Args:
        filename
        text
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
