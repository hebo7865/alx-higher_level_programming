#!/usr/bin/python3
"""Module of MyList class"""


class MyList(list):
    """Custom MyList class"""

    def print_sorted(self):
        """Method prints a sorted list"""
        print(sorted(self))
