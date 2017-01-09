# Problem 3
# Largest prime factor
#
# By Eunsol

import math

N = 600851475143
prime = [2];
all = [1] * int(math.sqrt(N))

for i in range(3, int(math.sqrt(N)), 2):
    if all[i]:
        for j in range(i * 3, int(math.sqrt(N)), i * 2):
            all[j] = 0
        prime.append(i)

for i in range(len(prime)):
    if N % prime[i] == 0:
        N /= prime[i]
        print(prime[i])
        continue

print (N)
