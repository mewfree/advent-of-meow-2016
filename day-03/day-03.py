#!/usr/bin/env python3

def possible_triangle(triangle_list):
    a = int(triangle_list[0])
    b = int(triangle_list[1])
    c = int(triangle_list[2])

    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# part 1
input = open('day-03.input', 'r')

count = 0
for line in input:
    clear_list = line.rstrip().split(' ')
    clear_list = list(filter(None, clear_list))
    if possible_triangle(clear_list):
        count += 1

print('part 1:')
print(count)

# part 2
input2 = open('day-03.input', 'r')

count2 = 0

tmp_list = [[], [], []]
for line in input2:
    clear_list = line.rstrip().split(' ')
    clear_list = list(filter(None, clear_list))
    if len(tmp_list[0]) < 3:
        tmp_list[0].append(clear_list[0])
        tmp_list[1].append(clear_list[1])
        tmp_list[2].append(clear_list[2])
    if len(tmp_list[0]) == 3:
        if possible_triangle(tmp_list[0]):
            count2 += 1
        if possible_triangle(tmp_list[1]):
            count2 += 1
        if possible_triangle(tmp_list[2]):
            count2 += 1
        tmp_list[0].clear()
        tmp_list[1].clear()
        tmp_list[2].clear()

print('part 2:')
print(count2)
