#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """append a string at the end of txt file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
