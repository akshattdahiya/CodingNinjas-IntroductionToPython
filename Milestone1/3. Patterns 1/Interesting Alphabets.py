from math import *
from collections import *
from sys import *
from os import *
n = int(input())
i = 1
p = n
while i<=n:
    j = 1
    while j<=i:
        x = ord('A')
        letter = chr(x + p + j - 2)
        print(letter , end="")
        j=j+1
    print()
    i = i+1
    p = p-1
