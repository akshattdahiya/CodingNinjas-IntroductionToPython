from os import *
from sys import *
from collections import *
from math import *
def ninjaPuzzle(n):
    i=1
    while i<=n:
        sp=1
        while sp<i:
            print(' ',end='')
            sp=sp+1
        j=1
        while j<=n-i+1:
            print('*',end='')
            j=j+1
        print()
        i=i+1
    return 0
