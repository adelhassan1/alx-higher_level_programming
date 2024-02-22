#!/usr/bin/python3
"""appending to file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    Args:
        filename
        text
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
