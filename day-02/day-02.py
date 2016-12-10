#!/usr/bin/env python3

# part 1
input = open('day-02.input', 'r')

# initials coordinates
coord = (0, 0)

def move(instruction):
    global coord
    x = coord[0]
    y = coord[1]

    if instruction == 'U' and y != 1:
        y += 1
    if instruction == 'D' and y != -1:
        y -= 1
    if instruction == 'R' and x != 1:
        x += 1
    if instruction == 'L' and x != -1:
        x -= 1

    coord = (x, y)

print('part 1:')
for line in input:
    instruction_list = list(line.rstrip())
    for instruction in instruction_list:
        move(instruction)
    print(coord)

# part 2
input2 = open('day-02.input', 'r')

# initials coordinates
coord2 = (-2, 0)

def move2(instruction):
    global coord2
    x = coord2[0]
    y = coord2[1]

    if instruction == 'U' and abs(x) + abs(y+1) <= 2:
        y += 1
    if instruction == 'D' and abs(x) + abs(y-1) <= 2:
        y -= 1
    if instruction == 'R' and abs(x+1) + abs(y) <= 2:
        x += 1
    if instruction == 'L' and abs(x-1) + abs(y) <= 2:
        x -= 1

    coord2 = (x, y)

print('part 2:')
for line in input2:
    instruction_list = list(line.rstrip())
    for instruction in instruction_list:
        move2(instruction)
    print(coord2)
