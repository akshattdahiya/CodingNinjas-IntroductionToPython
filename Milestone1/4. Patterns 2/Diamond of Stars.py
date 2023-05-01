from math import *
from collections import *
from sys import *
from os import *
n = int(input())
rows = n+1
i=1
while i<=n-1:
    space=1
    while space<= n-i:
        print(" " , end="")
        space+=1
    star = 1
    while star<= i:
        print("*" , end="")
        star+=1
    p=i-1
    while p>=1:
        print("*" , end="")
        p-=1
    print()
    i+=1
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(" " , end="")
        spaces+=1
    stars = 1
    while stars<=i:
        print("*" , end="")
        stars+=1
    p=i
    while p>=1:
        print("*" , end="")
        p-=1
    print()
    i+=1
