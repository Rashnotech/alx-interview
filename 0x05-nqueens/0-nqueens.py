#!/usr/bin/python3
"""a module that solves Nqueens"""
from sys import argv, exit


def is_safe(board, row, col):
    """
    Checks if placing a queen at (row, col) is safe,
    meaning no queen attacks it.
    """
    # Check same row and column
    for i in range(len(board)):
        if board[i] == col:
            return False
        elif board[i] is not None and abs(row - i) == abs(col - board[i]):
            return False
    return True


def solve_n_queens(board, row, solutions):
    """
    Solves the N-queens problem recursively, starting from the given row.
    Adds valid solutions to the provided list.
    """
    if row == len(board):
        # Append the solution to the list
        solutions.append(board.copy())
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, solutions)
            board[row] = None


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [None] * n
    solutions = []
    solve_n_queens(board, 0, solutions)
    # Print all solutions
    for solution in solutions:
        result = []
        for index, val in enumerate(solution):
            result.append([index, val])
        print(result)
