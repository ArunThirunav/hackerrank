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
    global i
    print("Enter: ")
    # print(ar)
    # A basic code for matrix input from user 

    n = int(input("Enter the number of rows:")) 

    # Initialize matrix 
    arr = [] 
    ar = []
    print("Enter the entries rowwise:") 

    # For user input 
    for i in range(n):		 # A for loop for row entries 
        a =[] 
        for j in range(n):	 # A for loop for column entries 
            a.append(int(input())) 
        arr.append(a) 

    # For printing the matrix 
    for i in range(n): 
        for j in range(n): 
            print(arr[i][j], end = " ") 
        print() 

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