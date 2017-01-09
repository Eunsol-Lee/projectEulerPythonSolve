# Problem 19
# Counting Sundays
#
# By Eunsol

# 1 Jan 1901: Tuesday

mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 2
count = 0
for year in range(1901, 2001):
    mon[2] = 29 if year % 4 == 0 else 28
    mon[2] = 28 if year % 400 == 0 else mon[2]
    for month in range(1, 13):
        if day % 7 == 0:
            count += 1
        day += mon[month]
        day %= 7

print (count)
