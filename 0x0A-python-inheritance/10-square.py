#!/usr/bin/python3
"""
Define square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class represent a square"""

    def __init__(self, size):
        """
        initialize the square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        method that returns the current square area
        """
        return self.__size * self.__size
