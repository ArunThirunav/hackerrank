import math
import os
import random
import re
import sys
from array import *
from itertools import combinations

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    print(n, k, ar)
    arr = (list(combinations(ar, 2)))
    count = 0
    for i in arr:
        print(i)
        s = sum(i)
        if s % k == 0:
            count += 1

    return count

if __name__ == '__main__':
  
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    
    result = divisibleSumPairs(n, k, ar)
    
"""
6 3
1 3 2 6 1 2
"""