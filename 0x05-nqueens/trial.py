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
    result = []
    pos = []
    solve_queens(N, 0, pos, result)
    return result


def solve_queens(size: int, row: int, pos: list, result: list) -> list:
    """
    A recursive function that solves nqueens
    Args:
        size: an integer value for board size
        row: an integer value for current row during program execution
        pos: a list that contain the placement of element in the board
        result: a list of possible solution after computations
    Return:
        a list of possible solution
    """
    print(f'result {result}')
    if row == size:
        result.append(pos[:])
        return
    else:
        for col in range(size):
            pos.append(col)
            solve_queens(size, row + 1, pos, result)
            if check_constraint(pos):
                #solve_queens(size, row + 1, pos, result)
                result.append(pos[:])
            else:
                pos.pop(len(pos) - 1)


def check_constraint(placement: list) -> bool:
    """
    A function that takes the placement of n queens if it's in
      diagonal, column or rows.
    Args:
        placement: a list of possible pos of the queens
    Return:
        True if it meets the constaint otherwise False
    """
    length = len(placement)

    for i in range(length):
        for j in range(i + 1, length):
            row_diff = abs(i - j)
            col_diff = abs(placement[i] - placement[j])
            if row_diff == col_diff:
                return False
    return True



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
        solutions = nqueens(N)
        for solution in solutions:
            print(solution)
