#!/bin/python3

import math
import os
import random
import re
import sys
from array import *
import collections

def getTotalX(a, b):
    factor_a = []
    
    for j in range(1,101):
        for i in a:
            if j % i == 0:
                factor_a.append(j)
    # print(factor_a)
    factor_a = [item for item, count in collections.Counter(factor_a).items() if count > 1]
    factor_b = []

    div = 0
    for j in factor_a:
        for i in b:
            if i % j == 0:
                div += 1
            
            if div == len(b):
                factor_b.append(j)
        div = 0
    
    print(factor_a)
    print(factor_b) 

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    arr = array('q', arr)

    brr = list(map(int, input().rstrip().split()))
    brr.sort()
    brr = array('q', brr)

    
    print(getTotalX(arr, brr))

"""
2 3
2 4
16 32 96

2 2
2 6
24 36
"""