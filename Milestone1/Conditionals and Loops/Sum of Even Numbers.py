n = int(input())
sum = 0
while n > 1:
    if n % 2 == 0:
        sum = sum + n
        n = n-2
         
    else:
        n = n - 1
        sum = sum + n
        n = n - 2
print(sum)
