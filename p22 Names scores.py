# Problem 22
# Names scores
#
# By Eunsol

import re

pattern = re.compile('"([A-Z]+)"')

f = open('p022_names.txt', 'r')
inp = f.readlines()
f.close()

names = pattern.findall(inp[0])
names.sort()

total = 0

for i in range(len(names)):
    total += sum(map(lambda x: ord(x) - 64, names[i])) * (i + 1)

print (total)
