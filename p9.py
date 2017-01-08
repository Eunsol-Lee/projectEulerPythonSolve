# Problem 9
# Special Pythagorean triplet
#
# By Eunsol

for a in range(1,334):
    for b in range(a,501):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print (a, b, c, a*b*c)
