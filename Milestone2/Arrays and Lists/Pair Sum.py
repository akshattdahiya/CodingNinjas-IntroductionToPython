from sys import stdin


def pairSum(arr, n, x) :
    count = 0
    i = 0
    while i < n:
        for j in range(i+1,n):
            if arr[i]+arr[j] == x:
                count += 1
        i += 1
    return count

def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1