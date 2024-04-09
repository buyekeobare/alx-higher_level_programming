#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): list of lists represent the chessboard.
    solutions (list): list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where row and column, are represnted by `r` and `c`  respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initializes an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for j in range(n)]
    [row.append(' ') for j in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Returns a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Returns the list of lists a representation of a solved chessboard."""
    solution = []
    for i in range(len(board)):
        for d in range(len(board)):
            if board[i][d] == "Q":
                solution.append([i, d])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for d in range(col + 1, len(board)):
        board[row][d] = "x"
    # X out all backwards spots
    for d in range(col - 1, -1, -1):
        board[row][d] = "x"
    # X out all spots below
    for i in range(row + 1, len(board)):
        board[i][col] = "x"
    # X out all spots above
    for i in range(row - 1, -1, -1):
        board[i][col] = "x"
    # X out all spots diagonally down to the right
    d = col + 1
    for i in range(row + 1, len(board)):
        if d >= len(board):
            break
        board[i][d] = "x"
        d += 1
    # X out all spots diagonally up to the left
    d = col - 1
    for i in range(row - 1, -1, -1):
        if d < 0:
            break
        board[i][d]
        d -= 1
    # X out all spots diagonally up to the right
    d = col + 1
    for i in range(row - 1, -1, -1):
        if d >= len(board):
            break
        board[i][d] = "x"
        d += 1
    # X out all spots diagonally down to the left
    d = col - 1
    for i in range(row + 1, len(board)):
        if d < 0:
            break
        board[i][d] = "x"
        d -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for d in range(len(board)):
        if board[row][d] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][d] = "Q"
            xout(tmp_board, row, d)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
