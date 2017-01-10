# Problem 30
# Digit fifth powers
#
# By Eunsol

import itertools

prod = itertools.product(range(10), repeat=6)

total = 0

for (a, b, c, d, e, f) in prod:
    if a*100000+b*10000+c*1000+d*100+e*10+f == a**5+b**5+c**5+d**5+e**5+f**5:
        print (a, b, c, d, e, f)
        total += a*100000+b*10000+c*1000+d*100+e*10+f

print (total-1)
