from math import *
from collections import *
from sys import *
from os import *
n = int(input())
i=1
while i<=n:
    spaces = 1
    while spaces <= n-i:
        print(' ' , end="")
        spaces+=1
    j=1
    p=i
    while p>=1:
        print(p , end="")
        p-=1
        j+=1
    x=i
    q=2
    while x <= i-1:
        print(q , end="")
        q-=1
        x+=1
    print()
    i+=1
