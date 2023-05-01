def checkMember(n):
    a,b=0,1
    temp=0
    d=0
    while temp<n:
        temp=a+b
        a=b
        b=temp
        d=temp
    return d==n
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
