# Problem 34
# Digit factorials
#
# By Eunsol

import itertools
import math
from functools import reduce

for i in range(2, 8):

    prod = itertools.product(range(0, 10), repeat = i)

    for (x) in prod:
        if x[0] and sum(map(math.factorial, x)) == reduce(lambda x, y: x*10+y, x):
            print (x)
