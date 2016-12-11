#!/usr/bin/env python3
from collections import Counter

input = open('day-06.input', 'r')

arr = []
for i in range(0, 8):
    arr.append([])

for line in input:
    line = line.rstrip()
    for index, char in enumerate(line):
        arr[index].append(char)

message = ''
message2 = ''
for i in range(0, 8):
    most_common = Counter(arr[i]).most_common()
    message += most_common[0][0]
    message2 += most_common[-1][0]

print('part 1:')
print(message)

print('part 2:')
print(message2)
