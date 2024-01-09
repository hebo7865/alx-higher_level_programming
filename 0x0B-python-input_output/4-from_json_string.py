#!/usr/bin/python3
"""Define from_json_string function"""


import json


def from_json_string(my_str):
    """return an object represented by json string"""
    return json.loads(my_str)
