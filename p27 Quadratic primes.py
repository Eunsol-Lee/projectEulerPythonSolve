# Problem 27
# Quadratic primes
#
# By Eunsol

import math

N = 1000000
prime = {2:1}
all = [1] * int(math.sqrt(N))

for i in range(3, int(math.sqrt(N)), 2):
    if all[i]:
        for j in range(i * 3, int(math.sqrt(N)), i * 2):
            all[j] = 0
        prime[i] = 1

largest = 0

for a in range(-999, 1001, 2):
    for b in range(-999, 1001, 2):
        n = 0
        while (n ** 2 + n * a + b) in prime:
            n += 1
            if n > largest:
                largest = n
                aa = a
                bb = b

print (largest, aa, bb, aa * bb)
