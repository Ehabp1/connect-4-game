board = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24" ,"25" ,"26" ,"27" ,"28" ,"29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51"]
# board of game
def display_board():
	print("|","0A","|","0B","|","0C","|","0D","|", "0E","|","0F","|","0G","|")
	print("_" * 36)	
	print("|"	,board[0],"|",board[ 1 ],"|",board[ 2],"|",board[ 3],"|",board[4 ],"|",board[ 5 ],"|",board[ 6],"|")
	print("_" * 36)	
	print("|",board[ 7],"|",board[8],"|",board[9],"|",board[10],"|", board[11],"|",board[12],"|",board[13],"|")
	print("_" * 36)	
	print("|",board[14],"|",board[15],"|",board[16],"|",board[17],"|",board[18],"|",board[19],"|",board[20],"|")
	print("_" * 36)	
	print("|",board[21],"|",board[22],"|",board[23],"|",board[24],"|",board[25],"|",board[26],"|",board[27],"|")
	print("_" * 36)
	print("|",board[28],"|",board[29],"|",board[30],"|",board[31],"|",board[32],"|",board[33],"|",board[34],"|")
	print("_" * 36)	
	print("|",board[35],"|",board[36],"|",board[37],"|",board[38],"|",board[39],"|",board[40],"|",board[41],"|")
	print("_" * 36)	
	



# put move of player1
def player1_move(move1):
	if move1 == "A":
		row= 35
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "XX"
				break
			else:
						row = row -7
	elif move1 == "B":
		row= 36
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "XX"
				break
			else:
						row = row -7
	elif move1 == "C":
		row= 37
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "XX"
				break
			else:
						row = row -7
	elif move1 == "D":
		row= 38
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "XX"
				break
			else:
						row = row -7	
	elif move1 == "E":
		row= 39
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "XX"
				break
			else:
						row = row -7			
	elif move1 == "F":
		row= 40
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "XX"
				break
			else:
						row = row -7	
	elif move1 == "G":
		row= 41
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "XX"
				break
			else:
						row = row -7	


# put move of player2
def player2_move(move2):
	if move2 == "A":
		row= 35
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "OO"
				break
			else:
						row = row -7
	elif move2 == "B":
		row= 36
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "OO"
				break
			else:
						row = row -7
	elif move2 == "C":
		row= 37
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "OO"
				break
			else:
						row = row -7
	elif move2 == "D":
		row= 38
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "OO"
				break
			else:
						row = row -7	
	elif move2 == "E":
		row= 39
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "OO"
				break
			else:
						row = row -7			
	elif move2 == "F":
		row= 40
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "OO"
				break
			else:
						row = row -7	
	elif move2 == "G":
		row= 41
		while True:
			if(board [row] != "XX") and (board[row] != "OO"):
				board[row] = "OO"
				break
			else:
						row = row -7	
def check_winner():
	#check column
	for i in range (0,7):
			if (board[i])==(board[i+7]) and (board[i])==(board[i+14]) and (board[i])==(board[i+21]):
				print("win")
				return True
				break
			elif (board[i+7]) ==(board[i+14]) and (board[i+7])==(board[i+21]) and(board[i+7])==(board[i+28]):
				print("win")
				return True
				break
			elif (board[i+14]) ==(board[i+21]) and (board[i+14])==(board[i+28]) and(board[i+14])==(board[i+35]):
				print("win")
				return True
				break
#check row
	for y in range (1,6):
		g= 36
		g= 36+1
		for j in range (y,g,8):
			if (board[j])==(board[j+1]) and (board[j])==(board[j+2]) and (board[i])==(board[j+3]):
					print("win")
					break
					return True
			elif (board[j+1]) ==( board[j+2]) and (board[j+1])==(board[j+3]) and(board[j+1])==(board[j+4]):
					print("win")
					return True
					break
			elif (board[j+2]) ==(board[j+3]) and (board[j+2])==(board[j+4]) and(board[j+2])==(board[j+5]):
					print("win")
					return True
					break
			elif (board[j+3]) ==(board[j+4]) and (board[j+3])==(board[j+5]) and(board[j+3])==(board[j+6]):
					print("win")
					return True
					break
	#check diagonal
	for r in range (0,4):
		if (board[r])==(board[r+8]) and (board[r])==(board[r+16]) and (board[r])==(board[r+24]):
				print("win")
				return True
				break
		elif (board[r+8]) ==(board[r+16]) and (board[r+8])==(board[r+24]) and(board[r+8])==(board[r+32]):
				print("win")
				return True
				break
		elif (board[r+16]) ==(board[r+24]) and (board[r+16])==(board[r+32]) and(board[r+16])==(board[r+40]):
			print("win")
			return True
			break
	for k in range (3,7):
		if (board[k])==(board[k+6]) and (board[k])==(board[k+12]) and (board[k])==(board[k+18]):
			print("win")
			return True
			break
		elif (board[k+7])==(board[k+13]) and (board[k+7])==(board[k+19]) and (board[k+7])==(board[k+25]):
			print("win")
			return True
			break
		elif (board[k+14])==(board[k+20]) and (board[k+14])==(board[k+26]) and (board[k+14])==(board[k+32]):
			print("win")
			return True
			break
	#Function play
def play():
	display_board()
	num=0
	while num < 42:
		move1 = input("choose letter from A:G(XX): ") 
		move1= move1 .upper()
		if (move1 != "A") and (move1 != "B") and  (move1 != "C") and (move1 != "D") and (move1 != "E") and (move1 != "F") and (move1 != "G") :
				move1 = input("NOT Valid!!!! please choose letter from A:G(OO): ") 
				move1= move1.upper()
				player1_move(move1)
		else:
			player1_move(move1)
		display_board()
		check_winner()
		if check_winner()==True:
			break
		else:
			move2 = input("choose letter from A:G(OO): ") 
			move2= move2.upper()
			if (move2 != "A") and (move2 != "B") and  (move2 != "C") and (move2 != "D") and (move2 != "E") and (move2 != "F") and (move2 != "G") :
				move2 = input("NOT Valid!!!! please choose letter from A:G: ") 
				move2= move2.upper()
				player2_move(move2)
			else:
				player2_move(move2)
			num = num+2	
			display_board()	
			if check_winner()==True:
				break
			else:
				continue
		print("draw")
		

play()