#!/usr/bin/python3
"""Module for is_same_class method"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of class"""
    return type(obj) is a_class
