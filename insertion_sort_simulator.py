import os
import time


def insertion_sort(l, n):
    for i in range(1, n, 1):
        time.sleep(0.5)
        key = l[i]
        j = i-1
        print("\nIteration ", str(i), ":")
        print("Before Pass :", *l, sep="\t")
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
        print("After Pass :", *l, sep="\t")

def execute_insertion_sort_simulator():
    os.system("cls")
    print("Insertion Sort Simulator")
    time.sleep(0.5)
    n = int(input("\n\nEnter number of elements of the array : "))
    l = list(map(int, input("Enter elements : ").split()))
    print("Original Array : ", end='')
    print(*l, sep="\t")
    print("\nInsertion Sort begins....")
    insertion_sort(l, n)
    time.sleep(0.5)
    print("\nSorted Array :", *l, sep="\t")
    time.sleep(0.5)
