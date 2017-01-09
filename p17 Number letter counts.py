# Problem 17
# Number letter counts
#
# By Eunsol

number = [0] * 1001;
number[1:21] = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3,
    6, 6, 8, 8, 7, 7, 9, 8, 8, 6]
numbers = [6, 5, 5, 5, 7, 6, 6, 7]
for i in range(3,11):
    number[i * 10] = numbers[i - 3]
for i in range(21, 100):
    if not number[i]:
        digit = int(i / 10) * 10
        number[i] = number[digit] + number[i % 10]
for i in range(100, 901, 100):
    number[i] = number[int(i / 100)] + 7
number[1000] = 11

for i in range(101, 1000):
    if not number[i]:
        digit = int(i / 100) * 100
        number[i] = number[digit] + 3 + number[i % 100]

print (sum(number[1:1001]))
print (number)
