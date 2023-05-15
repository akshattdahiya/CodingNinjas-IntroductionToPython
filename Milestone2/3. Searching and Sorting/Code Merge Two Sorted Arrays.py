from sys import stdin


def merge(arr1, n, arr2, m) :
    arr3 = []
    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i = i+1
        else:
            arr3.append(arr2[j])
            j = j+1
    while i < n:
        arr3.append(arr1[i])
        i = i+1
    while j < m:
        arr3.append(arr2[j])
        j = j+1
    return arr3

  
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0

  
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()

    
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
