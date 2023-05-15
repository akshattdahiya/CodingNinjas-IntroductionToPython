from sys import stdin

def rotate(arr, n, d):
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(n-d):
        arr[i] = arr[i+d]
    for i in range(d):
        arr[n-d+i] = temp[i]
    return arr


def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
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
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
