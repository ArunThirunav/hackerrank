from array import *
def sum(ar):
    max = len(ar) - 1
    print(ar[max])
    print(ar.count(ar[max]))
    

if __name__ == "__main__":
    global i
    ar = input("Enter: ")
    ar = list(map(int, ar.rstrip().split()))
    ar.sort()
    ar = array('Q', ar)
    print(ar)
    print(type(ar))
    sum(ar)
    # print(sum(ar))
