#!/usr/bin/python3
"""to_json_string"""


def save_to_json_file(my_obj, filename):
    """to_json_string"""
    import json

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
