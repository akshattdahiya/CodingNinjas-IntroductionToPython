from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output):
    i = n-1
    j = m-1
    carry = 0
    l = max(n, m)+1
    while i >= 0 and j >= 0:
        num = arr1[i]+arr2[j]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        i = i-1
        j = j-1
    while i >= 0:
        num = arr1[i]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        i = i-1
    while j >= 0:
        num = arr2[j]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        j = j-1
    if carry != 0:
        output[0] = carry


def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = (1 + max(n, m))
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1
