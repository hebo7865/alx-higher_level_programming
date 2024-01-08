#!/usr/bin/python3
"""Define a function that adds attributes to an object"""


def add_attribute(obj, attrib, value):
    """add new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrib, value)
