#!/usr/bin/python3
"""Object from json"""


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
        filename
    """
    import json
    with open(filename) as f:
        return (json.load(f))
