from sys import stdin

def pushZerosAtEnd(arr, n) :
    i = 0
    for x in range(i,n):
        if arr[x]!=0:
            arr[x],arr[i]=arr[i],arr[x]
            i+=1
    return arr
  
  
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1
