import math


with open("day9.txt") as f:
    lines = [
        tuple(int(x) for x in line.strip().split(","))
        for line in f
    ]

def get_sides(coord1, coord2):
    return tuple(abs(c2 - c1) for c1, c2 in zip(coord1, coord2))

max_area = 0
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        sides = get_sides(lines[i], lines[j])
        area = math.prod([side+1 for side in sides])
        max_area = max(max_area, area)

print(max_area)
