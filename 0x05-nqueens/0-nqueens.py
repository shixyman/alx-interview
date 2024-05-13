#!/usr/bin/python3
"""
Module 0-nqueens
A program that solves the N queens problem
"""
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check if there is a queen in the diagonal
        if board[i] - i == col - row or board[i] + i == col + row:
            return False

    return True


def solve_nqueens(board, row, N, solutions):
    if row == N:
        # Add the solution to the list
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen at the current position
            board[row] = col

            # Recur for the next row
            solve_nqueens(board, row + 1, N, solutions)


def format_solution(solution):
    formatted = [[row, col] for row, col in enumerate(solution)]
    return formatted


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
    board = [-1] * N

    # Solve the N-queens problem
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    # Format and print the solutions
    for solution in solutions:
        formatted_solution = format_solution(solution)
        print(formatted_solution)


if __name__ == '__main__':
    main()
