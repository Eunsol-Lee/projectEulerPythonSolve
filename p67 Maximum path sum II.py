# Problem 67 (similar to p18)
# Maximum path sum II
#
# By Eunsol

import math

f = open('p067_triangle.txt', 'r')
num = f.readlines()
f.close()

n = len(num)

m = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        m[i][j] = int(num[i - 1].split()[j - 1])

for i in range(2, n + 1):
    for j in range(1, i + 1):
        m[i][j] = max(m[i-1][j-1], m[i-1][j]) + m[i][j]

large = 0
for i in range(1, n + 1):
    large = max(large, m[n][i])

print (large)
