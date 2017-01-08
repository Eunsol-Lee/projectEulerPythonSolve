# Problem 10
# Summation of primes
#
# By Eunsol

import math

prime = [2];
all = [1] * 2000000

for i in range(3, 2000000, 2):
    if all[i]:
        for j in range(i * 3, 2000000, i * 2):
            all[j] = 0
        prime.append(i)

print(sum(prime))
