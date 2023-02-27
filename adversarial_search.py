"""
Problem: Implement adversarial search in the context of the game of Tic-Tac-Toe (X goes before O). The program should use the minimax algorithm with alpha-beta pruning and a heuristic evaluation function to determine the best move for the current player.

Specifically, your program should do the following:

Define a function minimax_alpha_beta_pruning that takes as input the current game state, the current player, and the maximum depth to search, and returns the best move for the current player using the minimax algorithm with alpha-beta pruning.

Define a function heuristic_evaluation that takes as input the current game state and the current player, and returns a score that estimates the desirability of the current state for the current player.

Define a function is_terminal_state that takes as input the current game state and returns True if the game is over and False otherwise.

Define a function get_valid_moves that takes as input the current game state and the current player, and returns a list of valid moves that the current player can make.

Define a function make_move that takes as input the current game state, the current player, and a move, and returns the new game state resulting from the move.

Write a main program that uses the functions defined above to implement the game of Tic-Tac-Toe and allows the user to play against the computer. The program should prompt the user to enter their move, update the game state, and display the updated board after each move.

To test your implementation, you can run your program and play Tic-Tac-Toe against the computer. You should be able to win if you play perfectly, but the computer should never lose if it plays perfectly as well.

Note: You can customize the heuristic evaluation function and the maximum search depth to improve the performance of your program and feel free to do different types of pruning.
"""
import copy
from typing import List, Tuple

def is_terminal_state(state: List[List[str]]) -> bool:
	"""
	Check if the Tic-Tac-Toe game is over.

	Parameters:
		state (list): The current game state represented as a 3x3 list of 'X', 'O', or ''.

	Returns:
		terminal (bool): True if the game is over, False otherwise.
	"""
	wins = [((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2))]

	for win in wins:
		win_list = []
		for cell in win:
			win_list.append(state[cell[0]][cell[1]])
		if win_list == ["X", "X", "X"] or win_list == ["O", "O", "O"]:
			return True
	return False

def winner(state: List[List[str]]) -> str:
	if not is_terminal_state(state): return ""
	else:
		wins = [((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2))]

		for win in wins:
			win_list = []
			for cell in win:
				win_list.append(state[cell[0]][cell[1]])
			if win_list == ["X", "X", "X"] or win_list == ["O", "O", "O"]:
				return win_list[0]
	return ""

def heuristic_evaluation(state: List[List[str]], player: str) -> int:
	"""
	Evaluate the desirability of a Tic-Tac-Toe game state for the given player.

	Parameters:
		state (list): The current game state represented as a 3x3 list of 'X', 'O', or ''.
		player (str): The player to evaluate the state for, either 'X' or 'O'.

	Returns:
		score (int): The desirability score for the current game state from the player's perspective.
	"""
	wins = [((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2))]
	win_count = 0

	if winner(state) == player: return 100

	for win in wins:
		cell_count = 0
		for cell in win:
			if state[cell[0]][cell[1]] == player or state[cell[0]][cell[1]] == "":
				cell_count += 1
		if cell_count == 3:
			win_count += 1
	
	return win_count

def get_valid_moves(state: List[List[str]], player: str) -> List[Tuple[int, int]]:
	"""
	Generate a list of valid moves for the current player in the given Tic-Tac-Toe game state.

	Parameters:
		state (list): The current game state represented as a 3x3 list of 'X', 'O', or ''.
		player (str): The current player, either 'X' or 'O'.

	Returns:
		valid_moves (list): A list of valid moves that the current player can make.
	"""
	moves = []

	for row in range(len(state)):
		for col in range(len(state[row])):
			if state[row][col] == "": moves.append((row, col))
	
	return moves

def make_move(state: List[List[str]], player: str, move: Tuple[int, int]) -> List[List[str]]:
	"""
	Make a move for the current player in the given Tic-Tac-Toe game state.

	Parameters:
		state (list): The current game state represented as a 3x3 list of 'X', 'O', or ''.
		player (str): The current player, either 'X' or 'O'.
		move (tuple): The row and column indices of the move to make.

	Returns:
		new_state (list): The new game state after the move is made.
	"""
	state[move[0]][move[1]] = player
	return state

def minimax_alpha_beta_pruning(state: List[List[str]], player: str, depth: int, alpha: float, beta: float, maximizing_player: bool) -> Tuple[float, Tuple[int, int]]:
	"""
	OPTIONAL: We could do something else for this as well feel free to do whatever. 
	Find the best move for the current player using the minimax algorithm with alpha-beta pruning.

	Parameters:
		state (list): The current game state represented as a 3x3 list of 'X', 'O', or ''.
		player (str): The player to find the best move for, either 'X' or 'O'.
		depth (int): The maximum search depth.
		alpha (float): The alpha value for alpha-beta pruning.
		beta (float): The beta value for alpha-beta pruning.
		maximizing_player (bool): True if the current player is the maximizing player, False otherwise.

	Returns:
		best_score (float): The score of the best move for the current player.
		best_move (tuple): The row and column indices of the best move.
	"""
	moves = get_valid_moves(state, player)

	if player == "X":
		other_player = "O"
	else:
		other_player = "X"

	if depth == 1:
		best_score = 0
		best_move = (0,0)

		if maximizing_player:
			for move in moves:
				if winner(make_move(copy.deepcopy(state), player, move)) == player:
					score = 1000
				else:
					score = heuristic_evaluation(make_move(copy.deepcopy(state), player, move), player) - heuristic_evaluation(make_move(copy.deepcopy(state), player, move), other_player)
				if score > best_score:
					best_score = score
					best_move = move

		else:
			for move in moves:
				if winner(make_move(copy.deepcopy(state), player, move)) == other_player:
					score = -1000
				else:
					score = heuristic_evaluation(make_move(copy.deepcopy(state), player, move), player) - heuristic_evaluation(make_move(copy.deepcopy(state), player, move), other_player)
				if score > best_score:
					best_score = score
					best_move = move
					
		return (best_score, best_move)

	else:
		if maximizing_player:
			best = (-10000,(0,0))
			for move in moves:
				score = minimax_alpha_beta_pruning(make_move(copy.deepcopy(state), player, move), player, depth-1, alpha, beta, not maximizing_player)
				if score[0] > best[0]:
					best = (score[0], move)
					
		else:
			best = (10000,(0,0))
			for move in moves:
				score = minimax_alpha_beta_pruning(make_move(copy.deepcopy(state), player, move), player, depth-1, alpha, beta, not maximizing_player)
				if score[0] < best[0]:
					best = (score[0], move)
		
		return best


def print_board(state: List[List[str]]) -> None:
	"""
	Print the current board """
	for row in state:
		for col in row:
			print(f"{col}\t", end="")
		print("\n")


game_board = [["X", "X", ""],
			  ["O", "", ""],
			  ["", "", ""]]

print(minimax_alpha_beta_pruning(game_board, "X", 2, -100, 100, True))