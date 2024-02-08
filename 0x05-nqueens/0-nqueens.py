#!/usr/bin/python3
"""a module that solve N queens puzzle challenge"""
from sys import argv, exit


def nqueens(N: int) -> list:
    """
    A function that place a non-attacking queens on an
    NxN chessboard
    Args:
        N: an integer value with lowest value of 4
    Returns:
        a list of an NxN
    """
    for i in range(N):

        for j in range(N):



if __name__ == '__main__':
    args_size = len(argv)
    N = int(argv[1])
    if args_size != 2:
        print('Usage: nqueens N')
        exit(1)
    elif not isinstance(N, int):
        print('N must be a number')
        exit(1)
    elif N < 4:
        print('N must be at least 4')
        exit(1)
    else:
        nqueens(N)
