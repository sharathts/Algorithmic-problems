import sys
row = 0
col = 0
n = int(raw_input("SIZE : "))
exit_flag = 0

#creates the board, all 0
def create_board():
    trial = [0] * n
    board = []
    for i in range(n):
        board.append(trial[:])
    return board
   
#Displays the board in a good format
def display_board(board):
    for i in range(n):
        for j in range(n):
            print board[i][j],
        print             
        
#marks the places in the board where the next queen cannot be placed
def colour_board(row, col, board, queen_num):

	for cur in range(n):
		if board[row][cur] == 0:
			board[row][cur] = queen_num
	for i in range(n):
		if board[i][col] == 0:
			board[i][col] = queen_num
	i = row
	j = col
	board[row][col] = 'Q'
	while (i >= 0 and j>= 0):
		i -= 1
		j -= 1
		if (board[i][j] == 0):
			board[i][j] = queen_num
	i = row
	j = col
	while (i >= 0 and j < n):
		if (board[i][j] == 0):
			board[i][j] = queen_num
		i -= 1
		j += 1

	i = row
	j = col
	while (i < n and j >= 0):
		if (board[i][j] == 0):
			board[i][j] = queen_num
		i += 1
		j -= 1
	
	i = row
	j = col
	while (i < n and j < n):
		if (board[i][j] == 0):
			board[i][j] = queen_num  
		i += 1
		j += 1
	queen_num += 1
	return board

#Finds a location in the board to place the queen, if any
def place_queen(board, queen_num):

    global exit_flag
    if exit_flag == 1:
        print "cannot place all queens."
        sys.exit()
    for row in range(n):
        if 0 in board[row]:
            temp = board[row]
            break

    for col in range(len(temp)):
        if temp[col] == 0:
            break
    if col == n-1 and row == 0:
        exit_flag = 1
        
    board = colour_board(row, col, board, queen_num)
    board[row][col] = 'Q'
    return [board, row, col]

#removes the slots blocked by the previous queen when a backtrack happens
def remove_paint(board, queen_num):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == queen_num:
				board[i][j] = 0	
	return board	

#Makes a good looking board, if after placing all queens
def filter_board(board):
	
	for i in range(len(board)):
		for j in range(len(board)):
			if (board[i][j]) != 'Q':
				board[i][j] = '-'
	return board

#A recursive procedure to place the queens
def process(board, queen_num, no_queens):

    if( queen_num > no_queens):
		return [board, 1]
    try:
        data = place_queen(board, queen_num)
        [board, flag] = process(data[0], (queen_num+1), no_queens)
        if flag == 0:
			board = remove_paint(board, (queen_num))
			row = data[1]
			col = data[2]
			if queen_num == 1:
			    board[row][col] = 99999;    
			else:
			    board[row][col] = (queen_num - 1) #not open to place queen
			[board, flag] = process(board, queen_num, no_queens)
			if flag == 0:
			    return [board, 0]
			else:
				return [board, 1]				
        else:
			return [board, 1]
#		print board
    except:
#		display_board(board)
#		print "back tracking"
		return [board, 0]



def main():
	no_queens = int(raw_input("Number of queens to be placed : "))
	board = create_board()
	[board, flag] = process(board, 1, no_queens)	
	board = filter_board(board)
	display_board(board)

if __name__=='__main__':
    main()
