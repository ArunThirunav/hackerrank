from array import array
def sum(ar):
    global i
    c, d, e = 0, 0, 0

    for i in ar:
        if i > 0:
            c += 1
        elif i < 0:
            d += 1
        else:
            e += 1
    print('{0:.5f}'.format(c/len(ar)))
    print(round((c/len(ar)),5))
    print(round((d/len(ar)),5))
    print(round((e/len(ar)),5))
    return (c, d, e)

if __name__ == "__main__":
    global i
    ar = input("Enter: ")
    ar = list(map(int, ar.rstrip().split()))
    ar = array('i', ar)
    print(ar)
    print(type(ar))
    print(sum(ar))
