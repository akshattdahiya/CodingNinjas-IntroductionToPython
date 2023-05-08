from sys import stdin

def sortZeroesAndOne(arr, n) :
    Zero = 0
    for i in range(n):
        if arr[i] == 0:
            arr[Zero], arr[i]= arr[i], arr[Zero]
            Zero += 1

def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()

t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
