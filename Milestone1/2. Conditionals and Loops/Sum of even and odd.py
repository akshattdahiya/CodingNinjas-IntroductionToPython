n = int(input())
e=0
o=0
while (n>0):
    a = n%10
    if (a%2==0):
        e= e+a
    else:
        o= o+a
    n = n//10
print(e, o)
