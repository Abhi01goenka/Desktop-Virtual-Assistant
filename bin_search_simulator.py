import os
import time

def binary_search(l, low, high, ele):
    i=0
    flag=-1
    while low <= high:
        i+=1
        time.sleep(0.5)
        print("\nIteration ",str(i), ":")
        mid=(low+high)//2
        print(*l[low:high+1], sep="\t")
        print("Middle element :",str(l[mid]))
        if ele>l[mid]:
            low=mid+1
            print("Going in the 2nd half of the array..")
        elif ele<l[mid]:
            high=mid-1
            print("Going in the 1st half of the array..")
        else:
            flag=mid
            break
    print("\n\n")
    if flag == -1:
        print(str(ele), "Not found..")
    else:
        print(str(ele), "found at index", str(flag))
        print("Number of iterations :",str(i))


    
def execute_bin_search_simulator():
    os.system("cls")
    print("Binary Search Simulator")
    time.sleep(0.5)
    n=int(input("\n\nEnter number of elements of the array : "))
    l=list(map(int,input("Enter elements in ascending order : ").split()))
    val=int(input("Enter element to be searched : "))
    print("\n\nBinary Search begins....")
    binary_search(l, 0, n-1, val)

