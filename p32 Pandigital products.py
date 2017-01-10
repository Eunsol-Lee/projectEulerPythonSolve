# Problem 32
# Pandigital products
#
# By Eunsol

# ## * ### = ####
# # * #### = ####


import itertools

prod = itertools.product(range(1,10), repeat=5)

result = set()

for (a, b, c, d, e) in prod:
    p = set(['0', str(a), str(b), str(c), str(d), str(e)])
    mul1 = str((a*10+b)*(c*100+d*10+e))
    mul2 = str((a)*(b*1000+c*100+d*10+e))
    if len(mul1) == 4 and len(p | set(mul1)) == 10:
        result.add(int(mul1))
    if len(mul2) == 4 and len(p | set(mul2)) == 10:
        result.add(int(mul2))

print (result)
print (sum(result))
