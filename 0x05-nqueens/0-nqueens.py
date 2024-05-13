#!/usr/bin/python3
"""
Module 0-nqueens
A program that solves the N queens problem
"""
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, N):
    if row == N:
        # All queens are placed, print the solution
        print_solution(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen at the current position
            board[row][col] = 'Q'

            # Recur for the next row
            solve_nqueens(board, row + 1, N)

            # Backtrack and remove the queen from the current position
            board[row][col] = '.'

def print_solution(board, N):
    for row in board:
        print(' '.join(row))
    print()

def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]

    # Solve the N-queens problem
    solve_nqueens(board, 0, N)

if __name__ == '__main__':
    main()