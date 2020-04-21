import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    u = 0
    count  = 0
    valley = 0
    for i in range (0,n):
        w = s[i]
        # print(w)
        if w == 'U':
            u += 1
        else:
            u -=1
        if u < 0 and valley == 0:
            count += 1
            valley = 1
        elif u == 0:
            valley = 0
        elif u > 0 and valley == 1:
            valley = 0
        print("w, u, count, valley: ", w, u, count, valley)
    # print (count)
    return count

if __name__ == '__main__':
    n = int(input())
    s = input()

    result = countingValleys(n, s)
    print(result)

"""
8
UDDDUDUU

ans: 1

12
DDUUDDUDUUUD

ans: 2
"""