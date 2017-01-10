# Problem 35
# Circular primes
#
# By Eunsol

prime = {2}
maxN = 1000000

def findPrimeNumber(N):
    v = [0] * (N + 1)
    for i in range(3, N+1, 2):
        if not v[i]:
            prime.add(i)
            for j in range(i*3, N+1, i*2):
                v[j] = 1

findPrimeNumber(maxN)

count = 0

for i in range(maxN):
    cache = 0
    target = i
    for j in range(len(str(i))):
        if not target in prime:
            cache = 1
        p = str(target)
        if target > 9 and p[1] == '0':
            cache = 1
        target = int(p[1:] + p[0])

    if not cache:
        count += 1

print (count)
