n = int(input())
i = 1
while i <= n:
    j = 1
    p = i
    while j<=i:
        x = ord('A')
        letter = chr(x + p - 1)
        print(letter , end="")
        j = j+1
        p = p+1
    print()
    i = i + 1
