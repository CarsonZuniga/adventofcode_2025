import sys
from collections import deque

with open("day10.txt") as f:
    lines = [line.strip() for line in f]

diagrams: list[tuple[bool, ...]] = []
schematics: list[tuple[tuple[int, ...], ...]] = []
joltages: list[list[int]] = []

for line in lines:
    diagram, *schematic_raw, joltage = line.split()
    diagrams.append(tuple(
        False if char == "." else True
        for char in diagram.strip("[]")
    ))
    schematics.append(tuple(
        tuple(int(x) for x in schematic.strip("()").split(","))
        for schematic in schematic_raw
    ))

    joltages.append([
        int(x) for x in joltage.strip("{}").split(",")
    ])

### Part 1 ###
def min_toggles(desired, schematic, start):
    desired = tuple(desired)
    start = tuple(start)
    schematic = tuple(tuple(piece) for piece in schematic)

    if start == desired:
        return 0

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, dist = queue.popleft()

        for piece in schematic:
            new_state = list(current)
            for idx in piece:
                new_state[idx] = not new_state[idx]
            new_state = tuple(new_state)

            if new_state == desired:
                return dist + 1

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, dist + 1))

    return sys.maxsize

result = 0
for diagram, schematic, joltage in zip(diagrams, schematics, joltages):
    result += min_toggles(diagram, schematic, [False] * len(diagram))

print(result)
