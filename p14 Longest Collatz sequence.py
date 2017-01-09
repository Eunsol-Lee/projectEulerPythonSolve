# Problem 14
# Longest Collatz sequence
#
# By Eunsol

num = {}
num[1] = 1

def seq(x):
    if x in num:
        return num[x]
    if x % 2:
        num[x] = seq(3 * x + 1) + 1
    else:
        num[x] = seq(x / 2) + 1
    return num[x]

largest = 0
for i in range(1, 1000001):
    if largest < seq(i):
        largest = seq(i)
        index = i

print (index, largest)
