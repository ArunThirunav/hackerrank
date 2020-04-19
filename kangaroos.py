#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    for i in range(0, 10000):
        x1 += v1
        x2 += v2 
        if x1 == x2:
            return "YES"
    return "NO"

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

"""
0 3 4 2
yes

0 2 5 3
no

"""
