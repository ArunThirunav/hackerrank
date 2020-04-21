#!/bin/python3

import math
import os
import random
import re
import sys
from array import array
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):

    a = []
    counter = list(Counter(arr).items())
    major = Counter(arr).most_common(1)

    for i in counter:
         a.append(i[1])

    a = array('q', a)
    return sum(a) - int(major[0][1])
    


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    print(result)

"""
3 3 2 1 3
"""