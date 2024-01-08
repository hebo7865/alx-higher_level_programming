#!/usr/bin/python3
"""Module for empty base geometry class"""


class BaseGeometry:
    """
    Base geometry class
    """
    def area(self):
        """Method that raises an exception msg"""
        raise Exception("area() is not implemented")
