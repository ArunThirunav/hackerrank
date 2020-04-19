#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from array import array

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    counter = Counter(arr)
    a = counter.most_common(1) 
    a = a[0][0] 
    print(type(counter))
    print(counter)
    print(a)

        
if __name__ == '__main__':

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    arr = array('q', arr)
    print(arr)
    result = migratoryBirds(arr)

"""
6
1 4 4 4 5 3

"""