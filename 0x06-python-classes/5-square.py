#!/usr/bin/python3
"""
Define square class
"""


class Square:
    """Class represent a square"""

    def __init__(self, size=0):
        """
        initialize the square size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        method that returns the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """getter for private inistance size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for private inistance size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with character #"""
        for i in range(self.size):
            for s in range(self.size):
                print("#", end="\n" if s is self.size - 1 and i != s else "")
        print()
