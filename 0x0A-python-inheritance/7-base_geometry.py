#!/usr/bin/python3
"""Module for empty base geometry class"""


class BaseGeometry:
    """
    Base geometry class
    """
    def area(self):
        """Method that raises an exception msg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
