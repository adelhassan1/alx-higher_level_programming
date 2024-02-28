#!/usr/bin/python3
"""object isinstance"""


def is_same_class(obj, a_class):
    """returns True if the object is instance of class
    Args
        obj - object
        a_class - class
    """
    if type(obj) is a_class:
        return True
    return False
