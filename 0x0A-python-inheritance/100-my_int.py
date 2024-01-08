#!/usr/bin/python3
"""
Define the class MyInt
"""


class MyInt(int):
    """is a rebel of int"""
    def __new__(cls, *args, **krgs):
        """new instance for the class"""
        return super(MyInt, cls).__new__(cls, *args, **krgs)

    def __eq__(self, other):
        """invert != with =="""
        return int(self) != other

    def __ne__(self, other):
        """invert == with !="""
        return int(self) == other
