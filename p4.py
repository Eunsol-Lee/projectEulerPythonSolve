# Problem 4
# Largest palindrome product
#
# By Eunsol

def palindrome(x):
    p = x
    q = 0
    while p:
        q = q * 10 + p % 10
        p = int(p / 10)
    return x == q


largest = 0
for i in range(999,100,-1):
    for j in range(i,100,-1):
        m = i * j
        if palindrome(m):
            largest = max(largest, m)

print (largest)
