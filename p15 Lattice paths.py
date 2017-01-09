# Problem 15
# Lattice paths
#
# By Eunsol

N = 20

m = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    m[0][i] = 1
    m[i][0] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        m[i][j] = m[i - 1][j] + m[i][j-1]

print (m[N][N])


import math

print (math.factorial(40) / math.factorial(20) / math.factorial(20))
