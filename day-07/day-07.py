#!/usr/bin/env python3
import re

input = open('day-07.input', 'r')

def supportsTLS(inside_brackets, outside_brackets):
    for string in inside_brackets:
        if hasABBA(string):
            return False

    for string in outside_brackets:
        if hasABBA(string):
            return True

    return False

def supportsSSL(inside_brackets, outside_brackets):
    ABAs = listABAs(''.join(outside_brackets))
    if hasCorrespondingBAB(''.join(inside_brackets), ABAs):
        return True

def hasABBA(string):
    strlist = list(string)
    for i in range(0, len(strlist)):
        if i > 0 and i < len(strlist)-2:
            if strlist[i] == strlist[i+1] and strlist[i-1] == strlist[i+2]:
                if strlist[i] != strlist[i-1]:
                    return True
def listABAs(string):
    abas = []
    strlist = list(string)
    for i in range(0, len(strlist)):
        if i < len(strlist)-2:
            if strlist[i] == strlist[i+2] and strlist[i] != strlist[i+1]:
                abas.append(''.join(strlist)[i:i+3])
    return abas

def hasCorrespondingBAB(string, ABAs):
    BABs = [x[1] + x[0] + x[1] for x in ABAs]

    for BAB in BABs:
        if BAB in string:
            return True

TLS_count = 0
SSL_count = 0
for line in input:
    line = line.rstrip()
    inside_brackets = re.findall(r'\[(\w+)\]', line)
    outside_brackets = [s.split(']')[-1] for s in line.split('[')]

    if supportsTLS(inside_brackets, outside_brackets):
        TLS_count += 1

    if supportsSSL(inside_brackets, outside_brackets):
        SSL_count += 1

print('part 1:')
print(TLS_count)

print('part 2:')
print(SSL_count)
