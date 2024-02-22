#!/usr/bin/python3
"""JSON of an object"""


def to_json_string(my_obj):
    """return the JSON
    Args:
        my_obj
    """
    import json
    return (json.dumps(my_obj, sort_keys=True))
