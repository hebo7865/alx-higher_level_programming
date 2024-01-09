#!/usr/bin/python3
"""Define pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tria = triangle[-1]
        tmp = [1]
        for i in range(len(tria) - 1):
            tmp.append(tria[1] + tria[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
