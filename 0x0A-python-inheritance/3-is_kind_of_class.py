#!/usr/bin/python3
"""object isinstance"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of
    or if the object is an instance of a class that inherited from
    Args
        obj - object to check
        a_class - class
    """
    if isinstance(obj, a_class):
        return True
    return False
