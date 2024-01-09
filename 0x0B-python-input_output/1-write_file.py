#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """Writes a string to txt file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
