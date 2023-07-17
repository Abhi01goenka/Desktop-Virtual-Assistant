import os
import time

def bubble_sort(l, n):
    for i in range(n-1):
        time.sleep(0.5)
        print("\nIteration ",str(i+1), ":")
        for j in range(n-i-1):
            time.sleep(0.5)
            print("\nPass", str(j+1), ":")
            print("Before Swap :",*l, sep="\t")
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
                print("Elements are swapped")
                print("After Swap :",*l, sep="\t")
            else:
                print("Elements are not swapped")
            
def execute_bubble_sort_simulator():
    os.system("cls")
    print("Bubble Sort Simulator")
    time.sleep(0.5)
    n=int(input("\n\nEnter number of elements of the array : "))
    l=list(map(int,input("Enter elements : ").split()))
    print("Original Array : ", end='')
    print(*l, sep="\t")
    print("\nBubble Sort begins....")
    bubble_sort(l, n)
    time.sleep(0.5)
    print("\nSorted Array :", *l, sep="\t")
    time.sleep(0.5)
