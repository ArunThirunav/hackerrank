#!/bin/python3

import math
import os
import random
import re
import sys
from array import *

# Complete the breakingRecords function below.
def breakingRecords(scores):
    print(scores)
    min  = scores[0]
    max = scores[0]
    minVal = 0
    maxVal = 0
    for i in range(1, len(scores)):
        if scores[i] < min:
            minVal += 1
            min = scores[i]
        elif scores[i] > max:
            maxVal += 1
            max = scores[i]
    return (maxVal, minVal)


if __name__ == '__main__':

    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    # scores.sort()
    scores = array('q', scores)
    breakingRecords(scores)
