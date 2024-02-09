#!/usr/bin/python3
import sys

def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe, meaning no queen attacks it.
  """
  # Check same row and column
  for i in range(len(board)):
      if board[i] == col:
          return False
      elif board[i] is not None and abs(row - i) == abs(col - board[i]):
          return False
  return True


def solve_n_queens(board, row):
  """
  Solves the N-queens problem recursively, starting from the given row.
  """
  if row == len(board):
    # Print the solution
    print("".join(map(str, board)))
    return
  
  for col in range(len(board)):
    if is_safe(board, row, col):
      board[row] = col
      solve_n_queens(board, row + 1)
      board[row] = None

def main():
  """
  Main function, checks arguments and calls the solver.
  """
  if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)
  
  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)
  
  if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)
  
  board = [[0] * n for _ in range(n)]
  solve_n_queens(board, 0)

if __name__ == "__main__":
  main()

