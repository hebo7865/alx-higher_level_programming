#!/usr/bin/python3
"""Define append_after function"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r", encoding="utf-8") as f:
        listLine = []
        while True:
            line = f.readline()
            if line == "":
                break
            listLine.append(line)
            if search_string in line:
                listLine.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(listLine)
