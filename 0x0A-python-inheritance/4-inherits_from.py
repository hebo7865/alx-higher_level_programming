#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """Return true if object is an instance of class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
