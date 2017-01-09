# Problem 21
# Amicable numbers
#
# By Eunsol

prime = [2];

def findPrime():
    limit = 20000
    all = [1] * limit
    for i in range(3, limit, 2):
        if all[i]:
            for j in range(i * 3, limit, i * 2):
                all[j] = 0
            prime.append(i)

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

def sumDivisor(x):
    total = 1
    for key in x.keys():
        p = 1
        for j in range(1, x[key] + 1):
            p +=  key ** j
        total *= p

    return total

findPrime()
total = 0

for i in range(2, 10000):
    div = findDivisor(i)
    inv = sumDivisor(div) - i
    invDiv = findDivisor(inv)
    if i == sumDivisor(invDiv) - inv and i != inv:
        print (i)
        total += i

print (total)
