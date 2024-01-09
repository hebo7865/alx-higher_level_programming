#!/usr/bin/python3
"""Define class_to_json function"""


def class_to_json(obj):
    """return the dictionary desciption for json"""
    return obj.__dict__
