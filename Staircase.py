from array import array
def sum(ar):
    for i in range(0,ar):
    # Inner loop 1
        for j in range(1,ar-i):
            print(" ",end="")
        # Inner loop 2
        for k in range(0,i+1):
            print("*",end="")
        print()
    

if __name__ == "__main__":
    ar = int(input("Enter: "))
    sum(ar)
