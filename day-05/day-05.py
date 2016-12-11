#!/usr/bin/env python3
import hashlib

door_id = 'abbhdwsy'
index = 0
password = ''

while len(password) < 8:
    str_bytes = bytes(door_id + str(index), encoding='utf-8')
    hash = hashlib.md5(str_bytes).hexdigest()

    if hash[:5] == '00000':
        password += hash[5]

    index += 1

print('part 1:')
print(password)

index2 = 0
password2 = ['', '', '', '', '', '', '', '']

while len(''.join(password2)) < 8:
    str_bytes = bytes(door_id + str(index2), encoding='utf-8')
    hash = hashlib.md5(str_bytes).hexdigest()

    if hash[:5] == '00000':
        position = hash[5]
        if position.isdigit() and int(position) < 8:
            if password2[int(position)] == '':
                password2[int(position)] = hash[6]

    index2 += 1

print('part 2:')
print(''.join(password2))
