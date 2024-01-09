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

    def to_json(self, attrs=None):
        """return the dictionary desciption for json"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        myDict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                myDict[key] = value
        return myDict
