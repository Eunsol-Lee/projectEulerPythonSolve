# Problem 24
# Lexicographic permutations
#
# By Eunsol

import math

def per(result, p, n):
    if n == 1:
        return result + ''.join(p)
    r = math.factorial(len(p) - 1)
    value = int((n - 0.0000001) / r)
    result += p[value]
    p = p[:value] + p[value + 1:]
    n -= value * r
    return per(result, p, n)

print (per('', '0123456789', 1000000))
