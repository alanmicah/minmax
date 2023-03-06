from hashlib import new
from tic_tac_toe import *
from copy import deepcopy

new_game = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

x_winning = [
	["X", "2", "O"],
	["4", "O", "6"],
	["7", "8", "X"]
]

o_winning = [
	["X", "X", "O"],
	["4", "X", "6"],
	["7", "O", "O"]
]

def game_is_over(board):
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

def evaluate_board(board):
  if has_won(board, "X"):
    return 1
  elif has_won(board, "O"):
    return -1
  else:
    return 0

def minimax(input_board, is_maximizing):
    # Base case - the game is over, so we return the value of the board
    if game_is_over(input_board):
        return evaluate_board(input_board)
    if is_maximizing:
        best_value = -float('Inf')
        symbol = "X"
    else:
        best_value = float('Inf')
        symbol = "O"
    for i in available_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, i, symbol)
    return new_board

print(minimax(x_winning, True))
