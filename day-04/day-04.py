#!/usr/bin/python3
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict): pass

input = open('day-04.input', 'r')

def getRoomString(line):
    return line.split('[')[0]

def getSectorId(line):
    return int(getRoomString(line).split('-')[-1])

def getRoomNameNoSpaces(line):
    return ''.join(getRoomString(line).split('-')[:-1])

def getRoomName(line):
    return ' '.join(getRoomString(line).split('-')[:-1])

def validateRoom(line):
    checksum = line.split('[')[1][:-1]

    alpha_sort = OrderedCounter(sorted(getRoomNameNoSpaces(line)))
    most_common = alpha_sort.most_common(5)
    calculated_checksum = ''.join([item[0] for item in most_common])

    if checksum == calculated_checksum:
        return True
    else:
        return False

key = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(string, n):
    result = ''

    for char in string:
        try:
            i = (key.index(char) + n) % 26
            result += key[i]
        except ValueError:
            result += char

    return result

count = 0
for line in input:
    line = line.rstrip()
    if validateRoom(line):
        count += getSectorId(line)
        if decrypt(getRoomName(line), getSectorId(line)) == 'northpole object storage':
            print('part 2:')
            print(getSectorId(line))

print('part 1:')
print(count)
