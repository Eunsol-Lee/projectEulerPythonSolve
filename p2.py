cache = [0] * 1000;

def fibo(x):
    if not cache[x]:
        cache[x] = x if x < 4 else fibo(x-1) + fibo(x-2)
    return cache[x];

sum = 0
i = 1
value = 0

while value < 4000000:
    value = fibo(i)
    i += 1
    if value % 2 == 0:
        sum += value

print (sum)
