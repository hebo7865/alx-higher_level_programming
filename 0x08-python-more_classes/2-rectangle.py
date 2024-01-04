#!/usr/bin/python3
"""
class that defines a rectangle
"""


class Rectangle:
    """class represent a rectangle"""
    def __init__(self, width=0, height=0):
        """intialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method return the area of rect"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method return the perimeter of rect"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2
