with open("day4.txt") as f:
    lines = [line.strip() for line in f.readlines()]

### Day 1 ###
def count_adjacent(grid, x, y):
    total = 0
    height = len(grid)
    width = len(grid[0])

    # All 8 direction offsets: (dx, dy)
    directions = [
        (-1, -1), (0, -1), (1, -1),  # above row
        (-1,  0),          (1,  0),  # same row
        (-1,  1), (0,  1), (1,  1),  # below row
    ]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # bounds check
        if 0 <= nx < width and 0 <= ny < height:
            if grid[ny][nx] == "@":
                total += 1

    return total

result = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "@":
            count = count_adjacent(lines, x, y)
            if count < 4:
                result += 1
print(result)
