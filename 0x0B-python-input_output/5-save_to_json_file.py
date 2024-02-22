#!/usr/bin/python3
"""write using JSON"""


def save_to_json_file(my_obj, filename):
    """creates an Object from a JSON file
    Args:
        my_obj
        filename
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(json.dumps(my_obj, sort_keys=True)))
