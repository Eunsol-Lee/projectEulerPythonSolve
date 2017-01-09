# Problem 20
# Factorial digit sum
#
# By Eunsol

import math

v = math.factorial(100)

print(sum(int(x) for x in str(v)))
