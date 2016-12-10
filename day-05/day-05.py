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

print(password)
