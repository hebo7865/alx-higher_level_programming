#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for i, s in enumerate(str):
        if i != n:
            newstr += s
    return newstr
