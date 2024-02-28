#!/usr/bin/python3
"""object isinstance"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args
        obj - object
        a_class - class
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
