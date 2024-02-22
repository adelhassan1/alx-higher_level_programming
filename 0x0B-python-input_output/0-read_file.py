#!/usr/bin/python3
"""Reading from a file"""


def read_file(filename=""):
    """reads a text file
    Args:
        filename
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read().rstrip())
