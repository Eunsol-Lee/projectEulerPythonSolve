# Problem 12
# Highly divisible triangular number
#
# By Eunsol

def findDivisor(x):
    p = {}

    i = 0;

    while x > 1:
        if not x % prime[i]:
            if not prime[i] in p:
                p[prime[i]] = 1
            else:
                p[prime[i]] += 1
            x /= prime[i]
        else:
            i += 1
    return p

def totalDivisors(x):
    a = findDivisor(x)
    b = findDivisor(x + 1)
    a.update(b)
    a[2] -= 1
    v = 1
    for value in a.values():
        v *= (value + 1)
    return v


target = 500

prime = [2];
all = [1] * 2000000

for i in range(3, 2000000, 2):
    if all[i]:
        for j in range(i * 3, 2000000, i * 2):
            all[j] = 0
        prime.append(i)


for i in range(2, 20000):
    if totalDivisors(i) > target:
        print (i, findDivisor(i), findDivisor(i + 1), i * (i + 1) / 2)
