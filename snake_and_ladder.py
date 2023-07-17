import time
import random
import os

def welcome_message(names):
    print("\n\n")
    time.sleep(0.5)
    print("Welcome!!", end=" ")
    time.sleep(0.3)
    print(*names, sep=", ")
    time.sleep(0.5)

def snake_bite(n):
    snake={99:15, 97:19, 92:54, 85:34, 71:32, 35:8, 29:10}
    if n in snake.keys():
        print("Bitten by snake!!")
        time.sleep(0.5)
        print(str(n),"-->",str(snake[n]))
        return snake[n]
    else:
        return n

def ladder_move(n):
    ladder={4:40, 27:56, 53:90, 59:95, 80:98}
    if n in ladder.keys():
        print("Found a ladder!!")
        time.sleep(0.5)
        print(str(n),"-->",str(ladder[n]))
        return ladder[n]
    else:
        return n

def dice():
    print("Dice is Rolled!!")
    r=random.randrange(1,7)
    time.sleep(1)
    print("Dice shows :",str(r))
    return r

def first_move(player_name, pos):
    r=dice()
    if r==6:
        return player_move(player_name, pos)
    else:
        return pos

def player_move(player_name, pos):
    r=dice()
    if r==6:
        return player_move(player_name, pos+r)
    else:
        return pos+r
    
def player_wins(player_name):
    print(player_name,"wins")

def execute_snake_and_ladder():
    player_win_position=[]
    os.system("cls")
    print("Snake and Ladder Game")
    time.sleep(0.5)
    no_of_players=int(input("\n\nEnter number of players : "))
    name_of_players=[]
    for i in range(no_of_players):
        time.sleep(0.2)
        print("Enter name of player",str(i+1),": ", end='')
        name=input()
        name_of_players.append(name)
    welcome_message(name_of_players)
    os.system("cls")
    print("Snake and Ladder Game")
    time.sleep(0.5)
    print("\n\nGame Begins!!")
    time.sleep(1)
    os.system("cls")
    print("Snake and Ladder Game")
    print("\n\n")
    position=[1]*no_of_players
    no_of_rounds=1
    while position.count(100)!=no_of_players-1:
        time.sleep(0.5)
        print("Round",str(no_of_rounds),":\n\n")
        no_of_rounds+=1
        for i in range(no_of_players):
            time.sleep(1)
            if position[i]==100:
                continue
            print(name_of_players[i],"move : ")
            new_position=position[i]
            if position[i]==1:
                new_position=first_move(name_of_players[i], position[i])
            else:
                new_position=player_move(name_of_players[i], position[i])
            if new_position>100:
                continue
            print(str(position[i]),"-->",str(new_position))
            position[i]=new_position
            if position[i]==100:
                player_win_position.append(name_of_players[i])
                player_wins(name_of_players[i])
                print("\n\n")
                continue
            position[i]=snake_bite(position[i])
            new_position=ladder_move(position[i])
            if new_position!=position[i]:
                new_position1=player_move(name_of_players[i], new_position)
                if new_position1>100:
                    continue
                print(str(new_position),"-->",str(new_position1))
                position[i]=new_position1
            if position[i]==100:
                player_win_position.append(name_of_players[i])
                player_wins(name_of_players[i])
                continue
            position[i]=snake_bite(position[i])
            print("\n\n")
        time.sleep(2.2)
        os.system("cls")
        print("Snake and Ladder Game")
        print("\n\n")

    print("Game Over!!")
    os.system("cls")
    print("Snake and Ladder Game")
    print("\n\n")
    print("Player Ranks :")
    for i in range(no_of_players-1):
        print(str(i+1),player_win_position[i], sep=" --> ")
    for i in range(no_of_players):
        if position[i]!=100:
            last_player=i
            break
    print(str(no_of_players),name_of_players[last_player], sep=" --> ")
    time.sleep(0.5)
    print("\n\nHope you enjoyed the Game!!")
    









