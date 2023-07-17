board=['-','-','-','-','-','-','-','-','-']
l10=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
game_on=True
winner=None
current_player='X'
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

def play_game():
    display_board()
    while(game_on):
        change_turn(current_player)
        check_game_over()
        flip_player()
    if(winner=='X' or winner=='O'):
        print("Winner is "+winner)
    elif(winner=="None"):
        print("There is a Tie")
        
def check_game_over():
    check_win()
    check_tie()

def check_win():
    global winner
    row=check_row()
    column=check_column()
    diagonal=check_diagonal()
    if(row):
        winner=row
    elif(column):
        winner=column
    elif(diagonal):
        winner=diagonal
    else:
        winner=None    
    return

def check_row():
    global game_on
    row1=board[0]==board[1]==board[2] != '-'
    row2=board[3]==board[4]==board[5] != '-'
    row3=board[6]==board[7]==board[8] != '-'
    if(row1 or row2 or row3):
        game_on=False
    if(row1):
        return board[0]
    elif(row2):
        return board[3]
    elif(row3):
        return board[6]
    

def check_column():
    global game_on
    col1=board[0]==board[3]==board[6] != '-'
    col2=board[1]==board[4]==board[7] != '-'
    col3=board[2]==board[5]==board[8] != '-'
    if(col1 or col2 or col3):
        game_on=False
    if(col1):
        return board[0]
    elif(col2):
        return board[1]
    elif(col3):
        return board[2]

def check_diagonal():
    global game_on
    d1=board[0]==board[4]==board[8] != '-'
    d2=board[6]==board[4]==board[2] != '-'
    if(d1 or d2):
        game_on=False
    if(d1):
        return board[0]
    elif(d2):
        return board[2]

def check_tie():
    global game_on
    if('-' not in board):
        game_on=False
    return

def change_turn(player):
    global l10
    print(player+"'s turn")
    pos=input("Enter a position from 1-9 : ")
    valid=False
    while(not valid):
        while(pos not in l10):
            pos=input("Enter a position from 1-9 : ")
        pos=int(pos)
        pos-=1
        if(board[pos]!='-'):
            print("Invalid move")
        else:
            valid = True

    board[pos]=player
    display_board()

def flip_player():
    global current_player
    if(current_player=='X'):
        current_player='O'
    elif(current_player=='O'):
        current_player='X'

def execute_tic_tac_toe():
    play_game()

# play_game()