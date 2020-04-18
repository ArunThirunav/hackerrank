a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(a)
print(len(a)-1)
pri = 0
sec = 0
for i, j in zip(a, (range(len(a)))):
    print(i)
    print(j)
    print(i[j])
    pri += i[j]

for i, j in zip(a, reversed(range(len(a)))):
    print(i)
    print(j)
    print(i[j])
    sec += i[j]

diff = abs(pri - sec)
print(diff)