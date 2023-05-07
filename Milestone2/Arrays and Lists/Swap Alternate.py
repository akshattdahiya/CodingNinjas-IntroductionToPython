from sys import stdin

def swapAlternate(arr, n) :
    l = len(arr)
    i = 0
    while i < l-1:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2 
    return arr

def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()

t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1
