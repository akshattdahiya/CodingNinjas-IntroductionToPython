from math import *
from collections import *
from sys import *
from os import *
n = int(input())
i=1
while i<=n:
    space=1
    while space<= n-i:
        print(" " , end="")
        space+=1
    j=1
    p=i
    while j<=i:
       print(p , end="")
       j+=1
       p+=1
    p=2*i - 2
    while p>=i:
        print(p , end="")
        p-=1
    print()
    i+=1
