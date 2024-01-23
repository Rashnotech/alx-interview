#!/usr/bin/python3
"""a module for minimum operator"""


def minOperations(n: int) -> int:
    """
    A function that calculate the fewest number of operations
    need to result in exactly number of character in a file
    Args:
        n: an integer value
    Returns:
        an integer value 0 if impossible to achieve
    """
    if not isinstance(n, int):
        return (0)
    count = 0
    divisor = 2
    while n >= divisor:
        if n % divisor == 0:
            count += divisor
            n /= divisor
        else:
            divisor += 1
    return count
