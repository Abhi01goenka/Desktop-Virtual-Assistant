import os
def execute_quiz_game():
    os.system("cls")
    print("Quiz Game\n\n\n")
    n = int(input("Number of questions "))
    lq = []
    la = []
    lp = []
    print("\n\n")
    for i in range(n):
        lq.append(input("Enter Question : "))
        la.append(input("Enter Answer   : "))
        lp.append(int(input("Enter Points   : ")))
        print("\n")
    os.system("cls")
    print("Quiz Time!!")
    print("\n\n")
    q = input("Do you want to play? ")
    if(q == "no" or q == "No" or q == "n"):
        quit()
    print("\n\n")
    points_earned = 0
    for i in range(n):
        print(lq[i])
        ans = input("Enter your Answer : ")
        if(ans == la[i]):
            print("Answer correct!!")
            points_earned += lp[i]
        else:
            print("Wrong Answer!!")
        print("\n\n")
    print("Points Earned : ", str(points_earned), "/", str(sum(lp)))
