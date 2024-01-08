#!/usr/bin/python3
"""
Module for rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass represent a rectangle"""
    def __init__(self, width, height):
        """intialise rectangle width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """public method that return the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """method represent String"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
