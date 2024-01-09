#!/usr/bin/python3
"""Define Student class"""


class Student:
    """
    class represent a student
    """
    def __init__(self, first_name, last_name, age):
        """initialize the student data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return the dictionary desciption for json"""
        return self.__dict__
