#!/usr/bin/python3
"""object isinstance"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args
        obj - object
        a_class - class
    """
    return issubclass(type(obj), a_class)
