import numpy as np
from copy import deepcopy

def print_sudoku(board):
    for row in board:
        print(row)

def generate_options(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def fix_solo(board):
    for i in range(9):
        for j in range(9):
            if isinstance(board[i][j], list) and len(board[i][j]) == 1:
                board[i][j] = board[i][j][0]
    return board

def is_solved(board):
    for row in board:
        for cell in row:
            if isinstance(cell, list):
                return False
    return True

def check_rows_columns(board):
    for i in range(9):
        for j in range(9):
            if isinstance(board[i][j], list):
                row_values = {board[i][k] for k in range(9) if isinstance(board[i][k], int)}
                col_values = {board[k][j] for k in range(9) if isinstance(board[k][j], int)}
                board[i][j] = [num for num in board[i][j] if num not in row_values and num not in col_values]
    return fix_solo(board)

def check_rects(board):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            fixed_values = {
                board[row][col]
                for row in range(box_row, box_row + 3)
                for col in range(box_col, box_col + 3)
                if isinstance(board[row][col], int)
            }
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    if isinstance(board[row][col], list):
                        board[row][col] = [num for num in board[row][col] if num not in fixed_values]
    return fix_solo(board)

def is_valid(board, row, col, num):
    for k in range(9):
        if board[row][k] == num or board[k][col] == num:
            return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_with_backtracking(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 or isinstance(board[i][j], list):
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_with_backtracking(board):
                            return True
                        board[i][j] = 0  # Backtrack
                return False
    return True

def solve(board):
    print_sudoku(board)
    board = generate_options(board)
    while not is_solved(board):
        previous = deepcopy(board)
        board = check_rows_columns(board)
        board = check_rects(board)
        if previous == board:
            break
    solve_with_backtracking(board)
    print("-----------------------")
    print_sudoku(board)
    return board


