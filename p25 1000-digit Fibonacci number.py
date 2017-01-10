# Problem 25
# 1000-digit Fibonacci number
#
# By Eunsol

cache = {1:1, 2:1}
def f(n):
    if not n in cache:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]

for i in range(1, 10000):
    if f(i) > 10 ** 999:
        print (i)
        break
