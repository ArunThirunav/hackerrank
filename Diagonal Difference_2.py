from array import array
import itertools
def sum(ar):
    global i
    pri = 0
    sec = 0

    for i, j in zip(ar,range(len(ar))):
        pri += i[j]

    for i, j in zip(ar,reversed(range(len(ar)))):
        sec += i[j]

    return abs(pri-sec)

if __name__ == "__main__":
    # print("Enter")
    n = (input("Enter: ").strip)
    print(n)
    print(len(n))
    # n = list(map(int, n.rstrip().split()))
    # n = array('L', n)
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split()))) 

    # For printing the matrix 
    for i in range(n): 
        for j in range(n): 
            print(arr[i][j], end = " ") 
        print() 

    print(len(arr))
    print(sum(arr))


"""
11
2
4
4
5
6
10
8
-12
11 2 4 4 5 6 10 8 -12"""