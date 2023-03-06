from re import M
from tic_tac_toe import *
from copy import deepcopy

my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]

# Python objects are saved in memory, and variables point to a location in memory.
# In this case, new_board, and my_board are two variables that point to the same object in memory.
new_board = my_board

# Use deepcopy function
new_board = deepcopy(my_board)

print(my_board[1][1])

# 5 is the centre of the board as the positions are given numbers,
# left to right, then up to down
select_space(new_board, 5, "O")
print_board(new_board)
print_board(my_board)
