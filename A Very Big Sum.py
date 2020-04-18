from array import array
def sum(ar):
    global i
    val = 0

    for i in ar:
        print(i)
        val += i
        # print("the value is :", val)

    return val

if __name__ == "__main__":
    global i
    ar = input("Enter: ")
    ar = list(map(int, ar.rstrip().split()))
    ar = array('Q', ar)
    print(ar)
    print(type(ar))
    print(sum(ar))
