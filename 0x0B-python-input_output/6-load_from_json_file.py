#!/usr/bin/python3
"""to_json_string"""


def load_from_json_file(filename):
    """to_json_string"""
    import json

    with open(filename, "r") as f:
        content = f.read()
        return json.loads(content)
