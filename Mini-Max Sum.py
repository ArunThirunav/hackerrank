from array import *
def sum(ar):
    max = 0
    maxList = []
    min = 0
    minList = []

    for i in range(0, len(ar)-1):
        minList.append(ar[i])
        min += ar[i]
    for j in reversed(range(1, len(ar))):
        max += ar[j]
        maxList.append(ar[j])

    # min = max - ar[0]
    print(maxList)
    print(minList)

    print(min, max)

if __name__ == "__main__":
    global i
    ar = input("Enter: ")
    ar = list(map(int, ar.rstrip().split()))
    ar.sort()
    ar = array('Q', ar)
    print(ar)
    print(type(ar))
    print(sum(ar))
