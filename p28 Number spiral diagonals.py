# Problem 28
# Number spiral diagonals
#
# By Eunsol

def cornerSum(k):
    return 1 if k == 1 else 4 * k ** 2 - 6 * (k - 1)

print (sum(map(cornerSum, range(1,1003,2))))
