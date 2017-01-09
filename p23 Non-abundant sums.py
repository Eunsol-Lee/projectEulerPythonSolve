# Problem 23
# Non-abundant sums
#
# By Eunsol

prime = [2];

def findPrime():
    limit = 30000
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

naList = []

for i in range(2, 28124):
    if sumDivisor(findDivisor(i)) - i > i:
        naList.append(i)

q = [0] * 28124
for i in range(len(naList)):
    for j in range(i, len(naList)):
        if naList[i] + naList[j] < 28124:
            q[naList[i] + naList[j]] = 1

total = 0
for i in range(28124):
    if q[i] == 0:
        total += i

print (total)
