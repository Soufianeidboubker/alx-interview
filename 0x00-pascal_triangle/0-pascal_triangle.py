#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    h = []
    if n <= 0:
        return h
    h = [[1]]
    for s in range(1, n):
        temp = [1]
        for n in range(len(h[s - 1]) - 1):
            curr = h[s - 1]
            temp.append(h[s - 1][n] + h[s - 1][n + 1])
        temp.append(1)
        h.append(temp)
    return h
