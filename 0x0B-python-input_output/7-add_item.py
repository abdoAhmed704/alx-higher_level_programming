#!/usr/bin/python3
"""script that adds all arguments to a Python list"""

import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

text_file = "add_item.json"
added = list(argv[1:])
try:
    my_list = load_from_json_file(text_file)
except Exception:
    my_list = []
my_list.extend(added)
save_to_json_file(my_list, text_file)
