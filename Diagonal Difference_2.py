#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(ar):
    # Write your code here
    pri = 0
    sec = 0

    for i, j in zip(ar,range(len(ar))):
        pri += i[j]

    for i, j in zip(ar,reversed(range(len(ar)))):
        sec += i[j]

    return abs(pri-sec)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
