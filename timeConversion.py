def timeConversion(s):
    b = s.split(":")
    hh = b[0]
    mm = b[1]
    ss = b[2][:2]
    c = b[2][-2:]
    print(hh)
    print(c)
    if c == 'PM' and  int(hh) != 12:
        hh = int(hh) + 12
    elif c == 'AM' and int(hh) == 12:
        print("elif")
        hh = "00"
    else:
        print("else")
        hh = hh
    print(hh)
    d = ("{}:{}:{}".format(hh, mm, ss))
    return d

if __name__ == '__main__':

    s = input() 
    print(type(s))
    print(timeConversion(s))