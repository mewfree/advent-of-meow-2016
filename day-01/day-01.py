#!/usr/bin/env python3
input = open('day-01.input', 'r').read()
instructions = input.split(', ')

# initials coordinates
coord = (0, 0, 'N')
all_coords = []

part2_done = False

def add_to_locations(origin_coord, destination_coord):
    global part2_done
    if origin_coord[0] == destination_coord[0]:
        every = 1
        if origin_coord[1] > destination_coord[1]:
            every = -1
        for i in range(origin_coord[1], destination_coord[1], every):
            if (origin_coord[0], i) in all_coords:
                print('part 2:')
                print(abs(origin_coord[0]) + abs(i))
                part2_done = True
            else:
                all_coords.append((origin_coord[0], i))
    else:
        every = 1
        if origin_coord[0] > destination_coord[0]:
            every = -1
        for i in range(origin_coord[0], destination_coord[0], every):
            if (i, origin_coord[1]) in all_coords:
                print('part 2:')
                print(abs(i) + abs(origin_coord[1]))
                part2_done = True
            else:
                all_coords.append((i, origin_coord[1]))

def walk(instruction):
    global coord
    x = coord[0]
    y = coord[1]
    facing = coord[2]

    direction = instruction[0]
    steps = int(instruction[1:])

    if facing == 'N':
        if direction == 'R':
            x += steps
            facing = 'E'
        else:
            x -= steps
            facing = 'W'
    elif facing == 'E':
        if direction == 'R':
            y -= steps
            facing = 'S'
        else:
            y += steps
            facing = 'N'
    elif facing == 'S':
        if direction == 'R':
            x -= steps
            facing = 'W'
        else:
            x += steps
            facing = 'E'
    else:
        if direction == 'R':
            y += steps
            facing = 'N'
        else:
            y -= steps
            facing = 'S'

    if part2_done == False:
        add_to_locations((coord[0], coord[1]), (x, y))

    coord = (x, y, facing)

# looping!
for instruction in instructions:
    walk(instruction)

# part 1
print('part 1:')
print(abs(coord[0]) + abs(coord[1]))
