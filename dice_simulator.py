import random
import time
import os 

def shape(n):
    print("[-----]")
    if n == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif n == 2:
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
    elif n == 3:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    elif n == 4:
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
    elif n == 5:
        print("[ 0 0 ]")
        print("[  0  ]")
        print("[ 0 0 ]")
    elif n == 6:
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
    print("[-----]")

def execute_dice_simulator():
    os.system("cls")
    print("Dice Simulator\n\n")
    print("Enter Y/y for rolling the dice.\nEnter N/n for exiting the simulator.\n\n")
    while(True):    
        choice=input("Enter your choice : ")
        if choice in "Yy":
            n=random.randrange(1,7)
            shape(n)
            print("The dice shows ",str(n))
            print("\n")
            time.sleep(0.5)
        else:
            print("Exiting the simulator.....")
            time.sleep(0.5)
            break
        
        