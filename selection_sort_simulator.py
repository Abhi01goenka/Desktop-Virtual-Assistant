import os
import time


def selection_sort(l, n):
    for i in range(n-1):
        time.sleep(0.5)
        min_idx = i
        print("\nIteration ", str(i+1), ":")
        m = min(l[i+1:])
        if m < l[min_idx]:
            min_idx = l.index(m)
        print("Before Swap :", *l, sep="\t")
        if min_idx != i:
            l[min_idx], l[i] = l[i], l[min_idx]
            print("Elements are swapped")
            print("After Swap :", *l, sep="\t")
        else:
            print("Elements are not swapped")

def execute_selection_sort_simulator():
    os.system("cls")
    print("Selection Sort Simulator")
    time.sleep(0.5)
    n = int(input("\n\nEnter number of elements of the array : "))
    l = list(map(int, input("Enter elements : ").split()))
    print("Original Array : ", end='')
    print(*l, sep="\t")
    print("\nSelection Sort begins....")
    selection_sort(l, n)
    time.sleep(0.5)
    print("\nSorted Array :", *l, sep="\t")
    time.sleep(0.5)
