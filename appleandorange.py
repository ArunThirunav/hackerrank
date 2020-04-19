import math
import os
import random
import re
import sys
from array import *
from itertools import cycle

def countApplesAndOranges(s, t, a, b, apples, oranges):
    c1 = 0
    c2 = 0
    for i in apples:
        applenewpos = int(i) + a
        if s <= applenewpos <= t:
            c1 +=1
    for j in oranges:    
        orangenewpos = int(j) + b
        if s <= orangenewpos <= t:
            c2 +=1
    
    print(applesNew, orangesNew)
    print(c1, c2)
    print(type(applesNew))
    return (c1, c2)  


if __name__ == '__main__':    
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    apples = array('i', apples)
    oranges = list(map(int, input().rstrip().split()))
    oranges = array('i', oranges)
    print(apples)
    print(type(apples))
    print(oranges)
    print(type(oranges))

    countApplesAndOranges(s, t, a, b, apples, oranges)

"""
7 11
5 15
3 2
-2 2 1
5 -6
"""