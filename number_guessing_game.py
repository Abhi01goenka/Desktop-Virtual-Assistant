import random
import os
import speech_recognition as s_r
import pyttsx3


def speech_input():
    r = s_r.Recognizer()
    with s_r.Microphone() as source:
        speak("Say a number!!")
        print("Say a number!! ", end="")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=2.5)
    # print(r.recognize_google(audio))
    # return r.recognize_google(audio)
    try:
        print("Recognizing! ", end="")
        num = r.recognize_google(audio, language="en-in")
        print(num)

    except Exception as e:
        speak("Say it again Please!!")
        return -1
    return num


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def execute_number_guessing_game():
    r = random.randrange(1, 101)
    os.system("cls")
    i = 1

    print("Number Guessing Game!!\n\n")
    speak("Number Guessing Game!!")

    while i <= 10:
        n = int(speech_input())
        while n == -1:
            print("\n\n")
            n = int(speech_input())
        if r < n:
            print("Number is lesser than the guessed number!!")
            speak("Number is lesser than the guessed number!!")
        elif r > n:
            print("Number is greater than the guessed number!!")
            speak("Number is greater than the guessed number!!")
        else:
            print("You guessed the number!!")
            speak("You guessed the number!!")
            print("The number is : ", str(r))
            print("Number of trials : ", str(i))
            break
        i += 1
        print("\n")
    if i > 10:
        print("You were not able to guess the number!!")
        speak("You were not able to guess the number!!")
