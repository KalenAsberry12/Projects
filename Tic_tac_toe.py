# global variables

# Game board
board = [ "-","-","-",
          "-","-","-",
          "-","-","-",]

# IF game is still going 
game_still_going = True

#who won? or tie?
winner = None

#whos turn is it 
current_player = "X"

# display board
def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])

#play a game at tic tac toe  
def play_game():

# Display intital board
  display_board()


# while the game is still going 
  while game_still_going:


# handle a single turn of an arbitrary player
    handle_turn(current_player)


# check if the game has ended
    check_if_game_over()
# flip to other player 
    flip_player()


    # The game has ended 
if winner == "X" or winner == "O":
  print(winner + " Won.")
elif winner == None:
  print("Tie.")




# Handle a single turn of an arbitrary player 
def handle_turn(player): 

  print(player + "'s turn.") 
  position = input("Choose a position from 1-9: ")
  


  while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    position = input("Invalid input. Choose a position from 1-9: ")
  
  position = int(position) - 1

  if board[position] != "-":
  
    print("You cant go there. Go again")

  board[position] = player

  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

# Set up global variables 
  global winner

  # check rows 
  row_winner = check_rows()
  # check columns
  columns_winner = check_columns()
  # check diagonals
  diagonals_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif columns_winner: 
   winner = columns_winner
  elif diagonals_winner: 
    winner = diagonals_winner
  else:
    #there was no win 
    winner = None 
  
  return



def check_rows():
  #set up global variables 
  global game_still_going 
  # check if any of thw rows have all the same vale (and is not empty)
  row_1 = board[0] == board[1]== board[2] != "-"
  row_2 = board[3] == board[4]== board[5] != "-"
  row_3 = board[6] == board[7]== board[8] != "-"

  # if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # return the winner (X or O) 
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_columns():
  global game_still_going 
  # check if any of thw rows have all the same vale (and is not empty)
  columns_1 = board[0] == board[3]== board[6] != "-"
  columns_2 = board[1] == board[4]== board[7] != "-"
  columns_3 = board[2] == board[5]== board[8] != "-"

  # if any columns does have a match, flag that there is a win
  if columns_1 or columns_2 or columns_3:
    game_still_going = False
  # return the winner (X or O) 
  if columns_1:
    return board[0]
  elif columns_2:
    return board[1]
  elif columns_3:
    return board[2]
  return
  


def check_diagonals():
  global game_still_going 
  # check if any of thw rows have all the same vale (and is not empty)
  diagonals_1 = board[0] == board[4]== board[8] != "-"
  diagonals_2 = board[6] == board[4]== board[2] != "-"
  

  # if any columns does have a match, flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
  # return the winner (X or O) 
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  
  
  return

def check_if_tie():
  return



def flip_player():
 # global variable we need
  global current_player
  # if the current player x, then change it to O
  if current_player == "X":
    current_player = "O"
  # If the current player was O, then change it to X 
  elif current_player =="O":
    current_player = "X" 
  return


play_game()
