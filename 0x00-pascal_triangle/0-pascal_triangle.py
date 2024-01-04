#!/usr/bin/python3
""" a module that solve pascal triangle problem"""


def pascal_triangle(n):
    """
        pascal_triangle: a function that compute pascal triangle
        n: is a positive integer value to generate output
        
        Return: an empty list if an n is less than 0 or equal 0.
    """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        tx_s = str(11 ** i)
        tx_list = []
        for num in tx_s:
            tx_list.append(num)
        pascal.append(tx_list)
    return pascal
    
