#!/usr/bin/python3
"""loads, adds and saves file"""
import sys
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

num = len(sys.argv)


try:
    mylist = load_from_json_file('add_item.json')
except ValueError:
    mylist = []

for i in range(1, num):
    mylist.append(sys.argv[i])
save_to_json_file(mylist, 'add_item.json')
