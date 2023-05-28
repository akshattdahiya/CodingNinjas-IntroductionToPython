from os import *
from sys import *
from collections import *
from math import *
def findGcd(x, y):
    while y:
        x, y = y, x % y
    return x
