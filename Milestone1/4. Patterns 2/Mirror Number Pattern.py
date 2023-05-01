n = int(input())
i = 1
while i<=n:
    space=1
    while space<=(n-i):
        print(" " , end="")
        space+=1
    num = 1
    while num<=i:
        print(num , end="")
        num+=1
    print()
    i+=1
