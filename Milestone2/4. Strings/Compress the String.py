s=input()
i=0
y=""
while i<len(s):
    x=s[i]
    j=i+1
    c=1
    while j<len(s) and s[j]==x:
        j=j+1
        c=c+1
    if c>1:
        y=y+s[i]+str(c)
    else:
        y=y+s[i]
    i=j
print(y)
