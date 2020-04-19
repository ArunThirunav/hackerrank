import math
import os
import random
import re
import sys
from array import array

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bcharged = sum(bill)//2
    bill.pop(k)
    ba = bill
    ba = array('q', ba)
    bactual = sum(ba)//2
    if bactual == b:
        print("Bon Appetit")
    else:
        print(bcharged-bactual)
    
    # print(bactual)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))
    bill = array('q', bill)

    b = int(input().strip())

    bonAppetit(bill, k, b)

"""
4 1
3 10 2 9
12

4 1
3 10 2 9
7
"""