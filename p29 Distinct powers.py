# Problem 29
# Distinct powers
#
# By Eunsol

def divisor(x):
    i = 2;
    div = {}
    while x > 1:
        if x % i == 0:
            x /= i
            if i in div:
                div[i] += 1
            else:
                div[i] = 1
        else:
            i += 1
    return div

allset = set()

for a in range(2,101):
    p = divisor(a)
    for b in range(2,101):
        q = {k: v * b for (k, v) in p.items()}
        allset.add(str(q))

print (len(allset))
