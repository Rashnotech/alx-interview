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
    if n <= 1:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n] if dp[n] != float('inf') else 0
