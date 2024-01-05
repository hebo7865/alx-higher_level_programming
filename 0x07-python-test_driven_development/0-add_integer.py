#!/usr/bin/python3
"""

Define add_integer method

"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: first integer
        b: seconed integer with default value of 98

    Raise:
        TypeError: if a or b is not int or float

    Return:
        Sum of two integer
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
