N = int(input())
rev = 0
while(N > 0):
    a = N % 10
    rev = rev * 10 + a
    N = N // 10
print(rev)
