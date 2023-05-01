n = int(input())
i=1
p=n
while i<=n:
    j=1
    while j <= (n - i + 1):
        print(p , end="")
        j+=1
    print()
    i+=1
    p-=1
