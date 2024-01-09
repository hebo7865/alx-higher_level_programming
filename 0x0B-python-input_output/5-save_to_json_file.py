#!/usr/bin/python3
"""Define save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a txt file using json"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
