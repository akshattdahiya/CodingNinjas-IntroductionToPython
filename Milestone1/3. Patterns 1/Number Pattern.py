from math import *
from collections import *
from sys import *
from os import *
n = int(input())
i = 1
p = n
while i<=n:
    j=1
    while j<=p:
        print(j , end="")
        j+=1
    print()
    i+=1
    p-=1
