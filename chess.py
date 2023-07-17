from termcolor import colored
import os
import time

# import speech_recognition as s_r
import pyttsx3


def display_board(board):
    for i in range(9):
        print("\n\n\t\t", end="")
        for j in range(8):
            if i != 0:
                if j != 0:
                    if "1" in board[i][j]:
                        print(board[i][j], "\t|\t", end="")
                    elif "2" in board[i][j]:
                        print(colored(board[i][j], "red"), "\t|\t", end="")
                    else:
                        print(board[i][j], "\t|\t", end="")

                else:
                    print(colored(board[i][j], "blue"), "\t\t", end="")
            else:
                print(colored(board[i][j], "blue"), "\t\t", end="")
        if i != 0:
            if "1" in board[i][8]:
                print(board[i][8], end="")
            elif "2" in board[i][8]:
                print(colored(board[i][8], "red"), end="")
        else:
            print(colored(board[0][8], "blue"), end="")
        print("\n")


def find_piece(piece, board):
    ind = " ABCDEFGH"
    for i in range(9):
        for j in range(9):
            if board[i][j] == piece:
                return ind[j] + str(i)


def which_piece(pos, board):
    ind = " ABCDEFGH"
    return board[int(pos[1])][ind.index(pos[0])]


def is_checkmate(dest, board):
    ind = " ABCDEFGH"
    piece = which_piece(dest, board)
    if piece[1] == "1":
        pos = find_piece("K2", board)
    else:
        pos = find_piece("K1", board)
    if piece[0] == "P":
        if abs(int(pos[1]) - int(dest[1])) == 1 and pos[0] == dest[0]:
            return True
        return False
    elif piece[0] == "E":
        if pos[0] == dest[0]:
            return True
        if pos[1] == dest[1]:
            return True
        return False
    elif piece[0] == "H":
        if (
            abs(ind.index(pos[0]) - ind.index(dest[0])) == 2
            and abs(int(pos[1]) - int(dest[1])) == 1
        ):
            return True
        if (
            abs(ind.index(pos[0]) - ind.index(dest[0])) == 1
            and abs(int(pos[1]) - int(dest[1])) == 2
        ):
            return True
        return False
    elif piece[0] == "C":
        if abs(ind.index(pos[0]) - ind.index(dest[0])) == abs(
            int(pos[1]) - int(dest[1])
        ):
            return True
        else:
            return False
    elif piece[0] == "K":
        if (
            abs(ind.index(pos[0]) - ind.index(dest[0])) == 0
            and abs(int(pos[1]) - int(dest[1])) == 1
        ):
            return True
        if (
            abs(ind.index(pos[0]) - ind.index(dest[0])) == 1
            and abs(int(pos[1]) - int(dest[1])) == 0
        ):
            return True
        if (
            abs(ind.index(pos[0]) - ind.index(dest[0])) == 1
            and abs(int(pos[1]) - int(dest[1])) == 1
        ):
            return True
        return False
    elif piece[0] == "Q":
        if pos[0] == dest[0]:
            return True
        if pos[1] == dest[1]:
            return True
        if abs(ind.index(pos[0]) - ind.index(dest[0])) == abs(
            int(pos[1]) - int(dest[1])
        ):
            return True
        return False


def valid_move(src, dest, board):
    ind = " ABCDEFGH"
    src_piece = which_piece(src, board)
    dest_piece = which_piece(dest, board)
    if "1" in src_piece and "1" in dest_piece:
        return False
    if "2" in src_piece and "2" in dest_piece:
        return False
    if src_piece in ["P1", "P2"]:
        if abs(int(src[1]) - int(dest[1])) == 1 and src[0] == dest[0]:
            return True
        else:
            return False
    if src_piece in ["E1", "E2"]:
        if src[0] == dest[0]:
            return True
        if src[1] == dest[1]:
            return True
        return False
    if src_piece in ["H1", "H2"]:
        if (
            abs(ind.index(src[0]) - ind.index(dest[0])) == 2
            and abs(int(src[1]) - int(dest[1])) == 1
        ):
            return True
        if (
            abs(ind.index(src[0]) - ind.index(dest[0])) == 1
            and abs(int(src[1]) - int(dest[1])) == 2
        ):
            return True
        return False
    if src_piece in ["C1", "C2"]:
        if abs(ind.index(src[0]) - ind.index(dest[0])) == abs(
            int(src[1]) - int(dest[1])
        ):
            return True
        else:
            return False
    if src_piece in ["K1", "K2"]:
        if (
            abs(ind.index(src[0]) - ind.index(dest[0])) == 0
            and abs(int(src[1]) - int(dest[1])) == 1
        ):
            return True
        if (
            abs(ind.index(src[0]) - ind.index(dest[0])) == 1
            and abs(int(src[1]) - int(dest[1])) == 0
        ):
            return True
        if (
            abs(ind.index(src[0]) - ind.index(dest[0])) == 1
            and abs(int(src[1]) - int(dest[1])) == 1
        ):
            return True
        return False
    if src_piece in ["Q1", "Q2"]:
        if src[0] == dest[0]:
            return True
        if src[1] == dest[1]:
            return True
        if abs(ind.index(src[0]) - ind.index(dest[0])) == abs(
            int(src[1]) - int(dest[1])
        ):
            return True
        return False


# def speech_input():
#     r = s_r.Recognizer()
#     with s_r.Microphone() as source:
#         speak("Tell your move!!")
#         print("Tell your move!! ", end="")
#         r.pause_threshold = 1
#         audio = r.listen(source, phrase_time_limit=5)

#     try:
#         print("Recognizing! ", end="")
#         choice = r.recognize_google(audio, language="en-in")
#         print(choice)

#     except Exception as e:
#         speak("Say it again Please!!")
#         print("\n")
#         return "None"
#     return choice


# def speech_input():
#     r = s_r.Recognizer()
#     with s_r.Microphone() as source:
#         speak("Tell your name")
#         print("Tell your name", end="")
#         r.pause_threshold = 1
#         audio = r.listen(source, phrase_time_limit=2.5)

#     try:
#         print("Recognizing! ", end="")
#         move = r.recognize_google(audio, language="en-in")
#         print(move)

#     except Exception as e:
#         speak("Say it again Please!!")
#         return "None"
#     return move


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_move(src, dest, board):
    piece = which_piece(src, board)
    if piece in ["P1", "P2"]:
        s = "Move Pawn from " + src + " to " + dest + "!!"
    elif piece in ["E1", "E2"]:
        s = "Move Rook from " + src + " to " + dest + "!!"
    elif piece in ["H1", "H2"]:
        s = "Move Knight from " + src + " to " + dest + "!!"
    elif piece in ["C1", "C2"]:
        s = "Move Bishop from " + src + " to " + dest + "!!"
    elif piece in ["K1", "K2"]:
        s = "Move King from " + src + " to " + dest + "!!"
    elif piece in ["Q1", "Q2"]:
        s = "Move Queen from " + src + " to " + dest + "!!"
    speak(s)


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def execute_chess():
    chess_board = [
        [" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H "],
        [1, "E1", "H1", "C1", "K1", "Q1", "C1", "H1", "E1"],
        [2] + ["P1"] * 8,
        [3] + ["  "] * 8,
        [4] + ["  "] * 8,
        [5] + ["  "] * 8,
        [6] + ["  "] * 8,
        [7] + ["P2"] * 8,
        [8, "E2", "H2", "C2", "K2", "Q2", "C2", "H2", "E2"],
    ]
    os.system("cls")
    print("Chess game")
    speak("Chess Game!!")
    time.sleep(0.5)
    # print("\n\nPlayer 1, ", end='')
    speak("Player 1, Enter your name!!")
    player1 = input("\n\nPlayer 1, Enter your name : ")
    # time.sleep(0.2)
    speak("Player 2, Enter your name!!")
    player2 = input("Player 2, Enter your name : ")
    time.sleep(0.5)
    print("\n\nWelcome!!", end=" ")
    speak("Welcome!!")
    time.sleep(0.2)
    print(player1, player2)
    s = player1 + " and " + player2
    speak(s)
    time.sleep(0.5)
    print("\n\nGame Begins!!")
    speak("Game Begins!!")
    time.sleep(1)
    os.system("cls")
    display_board(chess_board)
    ind = " ABCDEFGH"
    while True:
        s = player1 + "'s move!!"
        print(player1, "move : ", end="")
        speak(s)
        player1_move = input()
        # while player1_move == "NONE":
        #     player1_move = input().upper()
        # while len(player1_move)!=5 or player1_move[0] not in ['A','B','C','D','E','F','G','H'] or player1_move[1] not in [1,2,3,4,5,6,7,8] or player1_move[3] not in ['A','B','C','D','E','F','G','H'] or player1_move[4] not in [1,2,3,4,5,6,7,8]:
        #     player1_move = input().upper()
        if player1_move == "exit":
            s = player1 + " quits!! " + player2 + " wins!!"
            print(player2, "wins")
            speak(s)
            break
        while "1" not in which_piece(player1_move[0:2], chess_board):
            print("You can't move other player's piece!!")
            speak("You can't move other player's piece!!")
            time.sleep(0.5)
            os.system("cls")
            display_board(chess_board)
            s = player1 + "'s move!!"
            print(player1, "move : ", end="")
            speak(s)
            player1_move = input()
            # while player1_move == "NONE":
            #     player1_move = input().upper()
            # while len(player1_move)!=5 or player1_move[0] not in ['A','B','C','D','E','F','G','H'] or player1_move[1] not in [1,2,3,4,5,6,7,8] or player1_move[3] not in ['A','B','C','D','E','F','G','H'] or player1_move[4] not in [1,2,3,4,5,6,7,8]:
            #     player1_move = input().upper()
            if player1_move == "exit":
                s = player1 + " quits!! " + player2 + " wins!!"
                print(player2, "wins")
                speak(s)
                break
        if player1_move == "exit":
            s = player1 + " quits!! " + player2 + " wins!!"
            print(player2, "wins")
            speak(s)
            break
        while valid_move(player1_move[0:2], player1_move[3:], chess_board) == False:
            print("Invalid Move!!")
            speak("Invalid Move!!")
            time.sleep(0.5)
            os.system("cls")
            display_board(chess_board)
            s = player1 + "'s move!!"
            print(player1, "move : ", end="")
            speak(s)
            player1_move = input()
            # while player1_move == "NONE":
            #     player1_move = input().upper()
            # while len(player1_move)!=5 or player1_move[0] not in ['A','B','C','D','E','F','G','H'] or player1_move[1] not in [1,2,3,4,5,6,7,8] or player1_move[3] not in ['A','B','C','D','E','F','G','H'] or player1_move[4] not in [1,2,3,4,5,6,7,8]:
            #     player1_move = input().upper()
            if player1_move == "exit":
                s = player1 + " quits!! " + player2 + " wins!!"
                print(player2, "wins")
                speak(s)
                break
        if player1_move == "exit":
            s = player1 + " quits!! " + player2 + " wins!!"
            print(player2, "wins")
            speak(s)
            break
        speak_move(player1_move[0:2], player1_move[3:], chess_board)
        chess_board[int(player1_move[4])][ind.index(player1_move[3])] = chess_board[
            int(player1_move[1])
        ][ind.index(player1_move[0])]
        chess_board[int(player1_move[1])][ind.index(player1_move[0])] = "  "
        time.sleep(1)
        os.system("cls")
        display_board(chess_board)
        if is_checkmate(player1_move[3:], chess_board) == True:
            speak("Check!!")
        s = player2 + "'s move!!"
        print(player2, "move : ", end="")
        speak(s)
        player2_move = input()
        # while player2_move == "NONE":
        #     player2_move = input().upper()
        # while len(player2_move)!=5 or player2_move[0] not in ['A','B','C','D','E','F','G','H'] or player2_move[1] not in [1,2,3,4,5,6,7,8] or player2_move[3] not in ['A','B','C','D','E','F','G','H'] or player2_move[4] not in [1,2,3,4,5,6,7,8]:
        #     player2_move = input().upper()
        if player2_move == "exit":
            s = player2 + " quits!! " + player1 + " wins!!"
            print(player1, "wins")
            speak(s)
            break
        while "2" not in which_piece(player2_move[0:2], chess_board):
            print("You can't move other player's piece!!")
            speak("You can't move other player's piece!!")
            time.sleep(0.5)
            os.system("cls")
            display_board(chess_board)
            s = player2 + "'s move!!"
            print(player2, "move : ", end="")
            speak(s)
            player2_move = input()
            # while player2_move == "NONE":
            #     player2_move = input().upper()
            # while len(player2_move)!=5 or player2_move[0] not in ['A','B','C','D','E','F','G','H'] or player2_move[1] not in [1,2,3,4,5,6,7,8] or player2_move[3] not in ['A','B','C','D','E','F','G','H'] or player2_move[4] not in [1,2,3,4,5,6,7,8]:
            #     player2_move = input().upper()
            if player2_move == "exit":
                s = player2 + " quits!! " + player1 + " wins!!"
                print(player1, "wins")
                speak(s)
                break
        if player2_move == "exit":
            s = player2 + " quits!! " + player1 + " wins!!"
            print(player1, "wins")
            speak(s)
            break
        while valid_move(player2_move[0:2], player2_move[3:], chess_board) == False:
            print("Invalid Move!!")
            speak("Invalid Move!!")
            time.sleep(0.5)
            os.system("cls")
            display_board(chess_board)
            s = player2 + "'s move!!"
            print(player2, "move : ", end="")
            speak(s)
            player2_move = input()
            # while player2_move == "NONE":
            #     player2_move = input().upper()
            # while len(player2_move)!=5 or player2_move[0] not in ['A','B','C','D','E','F','G','H'] or player2_move[1] not in [1,2,3,4,5,6,7,8] or player2_move[3] not in ['A','B','C','D','E','F','G','H'] or player2_move[4] not in [1,2,3,4,5,6,7,8]:
            #     player2_move = input().upper()
            if player2_move == "exit":
                s = player2 + " quits!! " + player1 + " wins!!"
                print(player1, "wins")
                speak(s)
                break
        if player2_move == "exit":
            s = player2 + " quits!! " + player1 + " wins!!"
            print(player1, "wins")
            speak(s)
            break
        speak_move(player2_move[0:2], player2_move[3:], chess_board)
        chess_board[int(player2_move[4])][ind.index(player2_move[3])] = chess_board[
            int(player2_move[1])
        ][ind.index(player2_move[0])]
        chess_board[int(player2_move[1])][ind.index(player2_move[0])] = "  "
        time.sleep(1)
        os.system("cls")
        display_board(chess_board)
        if is_checkmate(player2_move[3:], chess_board) == True:
            speak("Check!!")
    os.system("cls")
    print("\n\n" "Thank you for playing.")
    speak("Thank you for playing.")
    print("Hope you enjoyed the game!!")
    speak("Hope you enjoyed the game!!")
