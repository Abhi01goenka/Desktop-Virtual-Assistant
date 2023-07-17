import time
import os
import random
import speech_recognition as s_r
import pyttsx3


def win(s1, s2):
    if s1 == "rock":
        if s2 == "rock":
            return "Tie"
        elif s2 == "paper":
            return "2"
        elif s2 == "scissors":
            return "1"
    elif s1 == "paper":
        if s2 == "rock":
            return "1"
        elif s2 == "paper":
            return "Tie"
        elif s2 == "scissors":
            return "2"
    elif s1 == "scissors":
        if s2 == "rock":
            return "2"
        elif s2 == "paper":
            return "1"
        elif s2 == "scissors":
            return "Tie"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speech_input():
    r = s_r.Recognizer()
    with s_r.Microphone() as source:
        speak("Say your move!!")
        print("Say your move!! ", end="")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=2.5)

    try:
        print("Recognizing! ", end="")
        move = r.recognize_google(audio, language="en-in")
        print(move)

    except Exception as e:
        speak("Say it again Please!!")
        return "None"
    return move


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def execute_rock_paper_scissors():
    os.system("cls")
    print("Rock, Paper and Scissors!!\n\n\n")
    speak("Rock, Paper and Scissors!!")
    speak("Enter your name!!")
    print("Enter your name : ", end="")
    name = input()
    s = "Welcome, " + name
    speak(s)
    speak("Enter number of rounds!!")
    no_of_rounds = int(input("Enter number of rounds : "))
    speak("Enter maximum points!!")
    max_points = int(input("Enter maximum points : "))
    user_rounds = 0
    computer_rounds = 0
    round = 0
    l = ["rock", "paper", "scissors"]
    os.system("cls")
    while no_of_rounds:
        round += 1
        r = "Round " + str(round) + " begins!!"
        print(r)
        speak(r)
        print("\n\n")
        no_of_rounds -= 1
        user_points = 0
        computer_points = 0
        while user_points != max_points and computer_points != max_points:
            ch = speech_input().lower()
            while ch == "none":
                print("\n\n")
                ch = speech_input().lower()
            while ch != "rock" and ch != "paper" and ch != "scissors":
                speak("Invalid choice!!")
                print("\n\n")
                ch = speech_input().lower()
            r = random.randrange(0, 3)
            print(name, "'s choice : ", ch, sep="")
            print("Computer's choice :", l[r])
            w = win(ch, l[r])
            if w == "1":
                outcome = ch + " beats " + l[r]
                print(outcome)
                speak(outcome)
                user_points += 1
            elif w == "2":
                outcome = l[r] + " beats " + ch
                print(outcome)
                speak(outcome)
                computer_points += 1
            else:
                speak("It's a Tie!!")
                print("Tie")
            print(user_points, computer_points)
            print("\n\n")
            time.sleep(1)
        r = "Round " + str(round) + " ends!!"
        print(r)
        speak(r)
        if user_points == max_points:
            result = name + " wins Round " + str(round)
            print(result)
            speak(result)
            user_rounds += 1
        elif computer_points == max_points:
            result = "Computer wins Round " + str(round)
            print(result)
            speak(result)
            computer_rounds += 1
        time.sleep(2)
        os.system("cls")

    print("Number of rounds won by", name, ": ", str(user_rounds))
    print("Number of rounds won by Computer : ", str(computer_rounds))
    if user_rounds > computer_rounds:
        s = name + " wins!!"
        print(s)
        speak(s)
    elif computer_rounds > user_rounds:
        print("Computer wins!!")
        speak("Computer wins!!")
    else:
        print("There is a Tie!!")
        speak("There is a Tie!!")
    print("\n\n" "Thank you for playing.")
    speak("Thank you for playing.")
    print("Hope you enjoyed the game!!")
    speak("Hope you enjoyed the game!!")
