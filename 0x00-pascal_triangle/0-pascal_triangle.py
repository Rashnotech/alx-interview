#!/usr/bin/python3
""" a module that solve pascal triangle problem"""


def pascal_triangle(n):
    """
    pascal_triangle: a function that compute pascal triangle
    n: is a positive integer value to generate output
    Return: an empty list if an n is less than 0 or equal 0.
    """
    if n <= 0:
        return pascal
    pascal = [[1]]
    for i in range(1, n):
        innerList = [1]
        for idx in range(len(pascal[i - 1]) - 1):
            innerList.append(pascal[i - 1][idx] + pascal[i - 1][idx + 1])
        innerList.append(1)
        pascal.append(innerList)
    return pascal
