#!/usr/bin/python3
#script that adds all arguments to a Python list
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import json
from sys import argv
my_list = []
text_file = "add_item.json"

try:
    my_list = load_from_json_file(text_file)
except:
    my_list = []

for indx in argv[1:]:
    my_list.append(indx)
save_to_json_file(my_list, text_file)