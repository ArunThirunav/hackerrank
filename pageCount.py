#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    print(n, p)
    midValue = n / 2

    if 1 <= p <= midValue and midValue > 1 and n > 2:
        return p // 2
    elif midValue < p <= n :
        if (n - p) >1:
            return (n - p) // 2
        else:
            return 1
    else:
        return 0

if __name__ == '__main__':

    n = int(input())
    p = int(input())

    result = pageCount(n, p)
    print(result)

"""
6
2

5
4

"""