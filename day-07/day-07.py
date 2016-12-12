#!/usr/bin/env python3
import re

input = open('day-07.input', 'r')

def supportsTLS(line):
    inside_brackets = re.findall(r'\[(\w+)\]', line)
    outside_brackets = [s.split(']')[-1] for s in line.split('[')]

    for string in inside_brackets:
        if hasABBA(string):
            return False

    for string in outside_brackets:
        if hasABBA(string):
            return True

    return False

def hasABBA(string):
    strlist = list(string)
    for i in range(0, len(strlist)):
        if i > 0 and i < len(strlist)-2:
            if strlist[i] == strlist[i+1] and strlist[i-1] == strlist[i+2]:
                if strlist[i] != strlist[i-1]:
                    return True

count = 0
for line in input:
    if supportsTLS(line.rstrip()):
        count += 1
print(count)
