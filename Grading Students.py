import math
import os
import random
import re
import sys
from array import *

grades_count = int(input().strip())

grades = []
ar = []

def gradingStudents(ar):
    res = []
    for i in ar:
        b = i % 5
        if b >= 3 and 100 >= i >= 38:
            c = i + (5 - b)
        elif b < 3 and 100 >= i > 38:
            c = i
        else:
            c = i

        res.append(c)
    print(res)
        
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

ar = array('i', grades)

print(ar)
print(type(ar))
gradingStudents(ar)

"""
4
73
67
54
38
33
39
41




31
32
33
34
35
36
37
38
39
40
41
52
63
72
76
81
90 
"""