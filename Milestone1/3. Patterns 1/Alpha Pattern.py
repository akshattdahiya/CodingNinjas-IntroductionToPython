from math import *
from collections import *
from sys import *
from os import *
n = int(input())
x = ord('A')
i = 1
while i<=n:
    j=1
    while j<=i:
        print(chr(x) , end="")
        j+=1
    print()
    i+=1
    x+=1
