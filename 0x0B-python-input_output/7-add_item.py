#!/usr/bin/python3
"""task 7"""

import sys
import os.path
import sys

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

myfile = "add_item.json"
json = []

if os.path.exists(myfile):
    json = load_from_json_file(myfile)

for arg in range(1, len(sys.argv)):
    json.append(sys.argv[arg])

save_to_json_file(json, myfile)
