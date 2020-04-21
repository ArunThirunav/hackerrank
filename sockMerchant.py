#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from array import array

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter = list(Counter(ar).items())
    resList = []
    for i in counter:

        if i[1] >= 2:
            match_pair = i[1] // 2
            print("i, match_pair: ", i, match_pair)
            resList.append(match_pair)
    resList = array('q', resList)
    print(resList)
    resList = sum(resList)
    return resList

        

if __name__ == '__main__':

    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)



 