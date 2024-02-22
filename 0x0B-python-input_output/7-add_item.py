#!/usr/bin/python3
import sys
import json
"""loads, adds and saves file"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    mylist = load_from_json_file('add_item.json')
except TypeError:
    mylist = []

for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])
save_to_json_file(mylist, 'add_item.json')
