from array import array
import itertools
def sum(a , b):
    global i
    c = 0
    d = 0
    val = array('i', [])
    for (i, j) in zip(a, b):
        print(i, j)
        if i>j:
            c +=1
        elif i<j:
            d +=1
        else:
            c = c
            d = d
    val.append(c)
    val.append(d)
    print(val)

    return val

if __name__ == "__main__":
    global i
    ar = input("Enter: ")
    br = input("Enter: ")
    a = list(map(int, ar.rstrip().split()))
    b = list(map(int, br.rstrip().split()))
    a = array('L', a)
    b = array('L', b)
    print(a, b)
    print(type(ar))
    sum(a , b)

    
# // 5 6 7
# 3 6 10
# 17 28 30
# 99 16 8