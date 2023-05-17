from math import *
from collections import *
from sys import *
from os import *
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))
