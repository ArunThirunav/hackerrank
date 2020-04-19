#!/bin/python3

import math
import os
import random
import re
import sys
from array import *

# Complete the birthday function below.
def birthday(s, d, m):
    print(s, d, m)
    count = 0
    cycle = 0
    if m > 1:
        sq = s[0]
        for i in range(1, len(s)):
            sq += s[i]
            cycle += 1
            if sq == d and cycle == m:
                count += 1

            sq = s[i]
        return count
    elif m == 1 and d == s[0]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))
    s = array('q', s)
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    # birthday(s, d, m)
    result = birthday(s, d, m)
    print(result)

"""
5
1 2 1 3 2
3 2

5
1 5 5 3 2
10 2

2

6
1 1 1 1 1 1
3 3

0

1
4
4 1

1

5
1 2 1 2 1
3 2
"""