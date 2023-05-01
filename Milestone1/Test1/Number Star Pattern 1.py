from os import *
from sys import *
from collections import *
from math import *
lines=int(input())
i=1  
while(i<=lines):
    j=lines  
    while (j>=1):
        if j!=i:  
            print(j, end='', flush=True)  
        else:  
            print('*', end='', flush=True)  
        j=j-1  
    print("")  
    i=i+1;
