#!/usr/bin/python3
"""add attribute"""


def add_attribute(obj, name, value):
    """a function that adds a new attribute
    Args
        cls - class
        name - name of the attribute
        value - value of the attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
