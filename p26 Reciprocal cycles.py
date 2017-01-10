# Problem 26
# Reciprocal cycles
#
# By Eunsol


def cycle(x):
    dic = {}
    a = 1
    count = 0
    while a:
        while a < x:
            a*= 10
            count += 1
        d = int(a/x)
        r = a % x
        if r in dic:
            return count - dic[r]
        else:
            dic[r] = count
        a = r

    return 0

largest = 0

for i in range(1, 1000):
    value = cycle(i)
    if value > largest:
        largest = value
        index = i

print (index)
