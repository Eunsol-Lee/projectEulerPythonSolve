# Problem 33
# Digit cancelling fractions
#
# By Eunsol

import itertools

prod = itertools.product(range(1,10), repeat = 3)

numerator = 1
denominator = 1
for (a, b, c) in prod:
    if (b*10+c)*a == (a*10+b)*c and a != b:
        print ('%d%d / %d%d = %d/%d' % (a, b, b, c, a, c))
        numerator *= a
        denominator *= c

print (denominator / numerator)
