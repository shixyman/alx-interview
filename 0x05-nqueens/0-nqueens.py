#!/usr/bin/python3
"""
Module 0-nqueens
A program that solves the N queens problem
"""
import sys


def solve_nqueens(n):
    def is_safe(board, row, col):
        # Check if a queen can be placed at the given position
        for i in range(row):
            if board[i] == col or \
                board[i] + i == col + row or \
                    board[i] - i == col - row:
                return False
        return True

    def place_queens(board, row):
        if row == n:
            # All queens are placed, print the solution
            print(board)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(board, row + 1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    place_queens(board, 0)


# Check the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

solve_nqueens(N)
