"""N-Queens problem solver using backtracking algorithm.

This script finds and prints all possible solutions for placing N queens on an N x N chessboard
such that no two queens threaten each other.
"""

def print_board(board):
    """Print the chessboard configuration."""
    for row in board:
        print("".join(row))
    print()

def safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col].

    Args:
        board (list of list of str): Current chessboard state.
        row (int): Row index to check.
        col (int): Column index to check.
        n (int): Size of the board (n x n).

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
def solve(board,row,n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if safe(board,row,col,n):
            board[row][col] = 'Q'
            solve(board,row + 1,n)
            board[row][col] = '.'
n=4
board=[["."for i in range(n)] for i in range(n)]
solve(board,0,n)