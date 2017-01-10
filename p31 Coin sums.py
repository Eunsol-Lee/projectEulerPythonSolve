# Problem 31
# Coin sums
#
# By Eunsol

# Dynamic programming
# f(money, coin) = money with last coin
#
#   0 1 2 3 4 5 6 7 8 9 10
# 1 1 1 1 1 1 1 1 1 1 1 1
# 2 1 1 2 2 3 3 4 4 5 5 6
# 5 1 1 2 2 3 4 5 6 7 8 10
#

pound = [1, 2, 5, 10, 20, 50, 100, 200]

money = 200

m = [[0] * (money + 1) for _ in range(len(pound) + 1)]
m[0][0] = 1 # = [1] * (money + 1)
for i in range(len(pound)):
    m[i + 1][0] = 1

for i in range(1, len(pound) + 1):
    for j in range(1, money + 1):
        m[i][j] = m[i - 1][j]
        if j - pound[i - 1] >= 0:
            m[i][j] += m[i][j - pound[i - 1]]

print (m[len(pound)][money])
