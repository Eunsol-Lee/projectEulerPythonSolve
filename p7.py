# Problem 7
# 10001st prime
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

print (prime[10000])
