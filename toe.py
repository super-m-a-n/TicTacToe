#Tic Tac Toe project with GUI because im bored
import sys
import random
from tkinter import *
from tkinter import messagebox

#GUI stuff
root = Tk()
root.title("Tic Tac Toe")

#Some global variables, may fix later(probably not)
###################################################
players_turn = False
game_over = False
cpu = 'X'  #Default cpu starts
player = 'O'
board = []
###################################################

#Functions

def initialize_game(player_starts):
	#initializes the buttons of the game-grid, the grid , who starts

	global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10
	global players_turn, cpu, player

	#Set who starts the game
	if player_starts:
		player = 'X'
		cpu = 'O'
		players_turn = True
	else:
		cpu = 'X'
		player = 'O'
		players_turn = False

	#build board, a matrix pararell to the gui grid
	board = create_board()

	#Build buttons (9 buttons for the tic tac toe board and one to tell the cpu to play)
	b1 = Button(root, text= ' ' , font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
	b2 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
	b3 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

	b4 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
	b5 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
	b6 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

	b7 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
	b8 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
	b9 = Button(root, text= ' ', font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

	b10 = Button(root, text= "CPU PLAY!", font=("Helvetica", 20), height=3, width=10, bg="SystemButtonFace", command=lambda: b_click(b10))

	#Grid our buttons to the screen
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

	b10.grid(row=1, column=3)

def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)
	b10.config(state=DISABLED)


def b_click(button):
	#function that decides what happens every time a button is clicked

	global players_turn, player, cpu, board, game_over

	if button["text"] == ' ' and players_turn == True: #checks for valid player move, and checks the state of the game (win or tie) afterwards
		button["text"] = player
		players_turn = False
		board = copy_grid(board)

		if is_winner(player,board):
			game_over = True
			messagebox.showinfo("Tic Tac Toe", "Player won the game\n")
			messagebox.showinfo("Tic Tac Toe", "CPU mission failed, we'll get em next time\n")
			disable_all_buttons()
			return

		if board_full(board):
			game_over = True
			messagebox.showinfo("Tic Tac Toe", "Game ends as a tie\n")
			disable_all_buttons()
			return

	elif button["text"] == "CPU PLAY!" and players_turn == False: #checks for valid computer move, and checks the state of the game (win or tie) afterwards
		board = cpu_make_move(cpu, player, board)
		players_turn = True

		if is_winner(cpu,board):
			game_over = True
			messagebox.showinfo("Tic Tac Toe", "CPU won the game\n")
			messagebox.showinfo("Tic Tac Toe", "Player mission failed, we'll get em next time\n")
			disable_all_buttons()
			return

		if board_full(board):
			game_over = True
			messagebox.showinfo("Tic Tac Toe", "Game ends as a tie\n")
			disable_all_buttons()
			return

	elif button["text"] != "CPU PLAY!" and players_turn == True and button["text"] != ' ':
		messagebox.showerror("Tic Tac Toe", "Square already taken, make another move\n")

	elif button["text"] == "CPU PLAY!" and players_turn == True:
		messagebox.showerror("Tic Tac Toe", "Not cpu turn, stop trying to crash my game\n")

	elif button["text"] != "CPU PLAY" and players_turn == False:
		messagebox.showerror("Tic Tac Toe", "Cpu turn to play, stop trying to crash my game\n")

def create_board():
	#creates board to be used pararell to the gui grid (the board will be an exact copy of the grid at all times)
	global board
	board = []
	for i in range(10):
		board.append(' ')
	return board

def is_winner(player, board):
	return ((board[1] == player and board[2] == player and board[3] == player) or
		   (board[4] == player and board[5] == player and board[6] == player) or
		   (board[7] == player and board[8] == player and board[9] == player) or
		   (board[1] == player and board[4] == player and board[7] == player) or
		   (board[2] == player and board[5] == player and board[8] == player) or
		   (board[3] == player and board[6] == player and board[9] == player) or
		   (board[1] == player and board[5] == player and board[9] == player) or
		   (board[3] == player and board[5] == player and board[7] == player))

def copy_grid(board):
	#the board will be used pararell to the gui grid and thus must be an exact copy of the grid at all times
	board[1] = b1["text"]
	board[2] = b2["text"]
	board[3] = b3["text"]
	board[4] = b4["text"]
	board[5] = b5["text"]
	board[6] = b6["text"]
	board[7] = b7["text"]
	board[8] = b8["text"]
	board[9] = b9["text"]
	return board

def change_grid_at(pos):
	global cpu
	if pos == 1:
		b1["text"] = cpu
	elif pos == 2:
		b2["text"] = cpu
	elif pos == 3:
		b3["text"] = cpu
	elif pos == 4:
		b4["text"] = cpu
	elif pos == 5:
		b5["text"] = cpu
	elif pos == 6:
		b6["text"] = cpu
	elif pos == 7:
		b7["text"] = cpu
	elif pos == 8:
		b8["text"] = cpu
	elif pos == 9:
		b9["text"] = cpu

def random_select(list):
	#returns random index from list
	return random.choice(list)

def is_empty(board, square):
	return board[square] == ' '

def board_full(board):
	for i in range(1,10):
		if board[i] == ' ':
			return False
	return True

def board_empty(board):
	count = 0
	for i in range(1,10):
		if is_empty(board,i):
			count = count + 1
	return count == 9

def cpu_make_move(cpu, player, board):

	potential_moves = [] #a list of all potential cpu moves as decided by our algorithm, then a random list element selector is called to randomize choice

	#step 0 of algorithm: opening move be played in center or corner
	if board_empty(board) == True:
		square = random_select([1,3,5,7,9])
		board[square] = cpu
		change_grid_at(square)
		return board

	#step 1 of algorithm : if there is a winner position for cpu, play it
	for i in range(1,10):
		if is_empty(board,i):
			board[i] = cpu
			if is_winner(cpu,board):
				potential_moves.append(i)
			board[i] = ' '

	if potential_moves:
		square = random_select(potential_moves)
		board[square] = cpu
		change_grid_at(square)
		return board

	#step 2 of algorithm : if there is a winner position for opponent, block it
	for i in range(1,10):
		if is_empty(board,i):
			board[i] = player
			if is_winner(player,board):
				board[i] = cpu
				change_grid_at(i)
				return board
			else:
				board[i] = ' '

	#step 3 of algorithm : if there is a fork opportunity, play it
	for i in range(1,10):
		count = 0 #counts ways to win for each move
		if is_empty(board,i):
			board[i] = cpu
			for j in range(1,10):
				if is_empty(board,j):
					board[j] = cpu
					if is_winner(cpu,board):
						count = count + 1
					board[j] = ' '

			if count > 1: #checks if there is indeed a fork (two ways to win after move)
				potential_moves.append(i)
			board[i] = ' '

	if potential_moves:
		square = random_select(potential_moves)
		board[square] = cpu
		change_grid_at(square)
		return board

	#step 4 of algorithm : if there is a fork oppportunity for opponent, block it
	for i in range(1,10):
		count = 0
		if is_empty(board,i):
			board[i] = player
			for j in range(1,10):
				if is_empty(board,j):
					board[j] = player
					if is_winner(player,board):
						count = count + 1
					board[j] = ' '

			if count > 1: #checks if there is indeed a fork (two ways to win after move)
				potential_moves.append(i)
			board[i] = ' '

	if len(potential_moves) == 1: #if there is only one possible opponent fork, then block it
		board[potential_moves[0]] = cpu
		change_grid_at(potential_moves[0])
		return board

	elif len(potential_moves) > 1: #if there are more than one potential opponent forks, then cpu makes a move to make opponent defend, while avoiding forks
		potential_moves = []
		for i in range(1,10):
			count = 0
			if is_empty(board,i):
				board[i] = cpu
				for j in range(1,10):
					if is_empty(board,j):
						board[j] = cpu
						if is_winner(cpu,board):
							board[j] = player
							for k in range(1,10):
								if is_empty(board,k):
									board[k] = player
									if is_winner(player,board):
										count = count + 1
									board[k] = ' '
							if count <= 1:
								potential_moves.append(i)
						board[j] = ' '
				board[i] = ' '

	if potential_moves:
		square = random_select(potential_moves)
		board[square] = cpu
		change_grid_at(square)
		return board

	#step 5 of algorithm : cpu marks the center
	center = 5
	if is_empty(board,center) == True:
		board[center] = cpu
		change_grid_at(center)
		return board

	#step 6 of algorithm: cpu plays an opposite corner
	if board[1] == player and is_empty(board,9):
		potential_moves.append(9)
	elif board[9] == player and is_empty(board,1):
		potential_moves.append(1)
	elif board[3] == player and is_empty(board,7):
		potential_moves.append(7)
	elif board[7] == player and is_empty(board,3):
		potential_moves.append(3)

	if potential_moves:
		square = random_select(potential_moves)
		board[square] = cpu
		change_grid_at(square)
		return board

	#step 7 of algorithm : cpu marks an empty square
	if is_empty(board,1):
		potential_moves.append(1)
	elif is_empty(board,3):
		potential_moves.append(3)
	elif is_empty(board,7):
		potential_moves.append(7)
	elif is_empty(board,9):
		potential_moves.append(9)

	if potential_moves:
		square = random_select(potential_moves)
		board[square] = cpu
		change_grid_at(square)
		return board

	#step 8 of algorithm : cpu marks the middle of any of the 4 sides
	for i in range(2,9,2):
		if is_empty(board,i):
			potential_moves.append(i)

	if potential_moves:
		square = random_select(potential_moves)
		board[square] = cpu
		change_grid_at(square)
		return board








###########################################################################################

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu )
options_menu.add_command(label="Reset Game: Computer starts", command=lambda: initialize_game(0))
options_menu.add_command(label="Reset Game: Player starts", command=lambda: initialize_game(1))

#main program
initialize_game(0)

root.mainloop()
