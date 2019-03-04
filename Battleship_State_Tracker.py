import numpy as np
import sys

#Function that creates an empty board
def create_board(boardsize):
	board = [[0 for i in range(boardsize)] for j in range(boardsize)]	
	print("New board has been created for this game")
	return board

#Function that checks the presence of a ship between the given range - (x1,y1) to (x2,y2)
def ship_present(board,x1,y1,x2,y2):	
	if x1 == x2:
		for y in range(y1,y2):
			if board[x1][y] == 1:
				print("Cannot place ship here")
				return True
	elif y1 == y2:
		for x in range(x1,x2):
			if board[x][y1] == 1:
				print("Cannot place ship here")
				return True	
	return False

#Adds a battleship to the given board
def add_battleship(board,boardsize):
	print("Enter the size of battleship, which is lesser than or equal to "+ str(boardsize))
	size = int(sys.stdin.readline())
	if size > boardsize or size <= 0:
		print("Invalid size of battleship")
		return
	
	print("Enter the starting coordinates of the battleship as <x> space <y>")
	x,y = list(map(int,sys.stdin.readline().split()))
	#Resetting x and y such that the board coordinates starts from 1 instead of 0 - Just for better readability
	x = x-1; y = y-1
	if x<0 or y<0 or x >= boardsize or y >= boardsize:
		print("Invalid coordinates")
		return
	
	if x+size > boardsize:
		if y+size > boardsize:
			print("This battleship cannot be placed from the starting coordinates mentioned as its size exceeds the boardsize.")
			return
		else:
			#print("Placing ship Horizontly ")
			direction = 'H'
	elif y+size > boardsize:
		#print("Placing ship Vertically")
		direction = 'V'
	else:
		print("Enter H for placing battleship Horizontly and V for placing the battleship Vertically ")
		direction = sys.stdin.readline().strip().split(" ")[0]

	if direction == 'H' or direction == 'h':		
		row = x
		if not ship_present(board,x,y,x,y+size):			
			for col in range(y,y+size):
				board[row][col] = 1
			print("Ship placed Horizontly ")
	
	elif direction == 'V' or direction == 'v':
		col = y
		if not ship_present(board,x,y,x+size,y):			
			for row in range(x,x+size):
				board[row][col] = 1
			print("Ship placed Vertically")
	
	else:
		print("Invalid entry - Ship couldnt be placed")
		return

	return board

#Takes an attack at a given position and returns HIT or MISS. If its a hit, alters the board to denote the hit.
def attack(board,x,y):
	if board[x][y] == 1:
		print("Attck resulted in a HIT")
		board[x][y] = 0
	else:
		print("Attack resulted in a MISS")
	return board

#Returns whether the player lost the game or not.
def game_state(board):
	for row in board:
		for val in row:
			if val == 1:
				print("Game status: Player hasnt lost the game yet")
				return
	print("Game status: No battleship in board, Player lost the game")
	return


boardsize = 10
board = create_board(boardsize)

print("Do you want to add a battleship? (y,yes or no,n)")
char = sys.stdin.readline().strip().split(" ")[0]

while char == 'y' or char == 'yes':
	add_battleship(board,boardsize)
	print("Do you want to add another battleship? (y,yes or no,n)")
	char = sys.stdin.readline().strip().split(" ")[0]

print("Do you want to take an attack? (y,yes or no,n)")
char = sys.stdin.readline().strip().split(" ")[0]

while char == 'y' or char == 'yes':
	print("Enter attack coordinates X space Y")
	x,y = list(map(int,sys.stdin.readline().split()))
	x = x-1; y = y-1	
	
	if x<0 or y<0 or x >= boardsize or y >= boardsize:
		print("Invalid coordinates")
	else:
		attack(board,x,y)

	print("Do you want to take more attacks ?(y,yes or no,n)")
	char = sys.stdin.readline().strip().split(" ")[0]

game_state(board)
print(np.matrix(board))

