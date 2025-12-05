ranges = []
ids = []
in_ids = False

with open("day5.txt") as f:
    for line in f.readlines():
        if not line.strip():
            in_ids = True
            continue
        if not in_ids:
            parts = line.strip().split("-")
            ranges.append((int(parts[0]), int(parts[1])))
        else:
            ids.append(int(line.strip()))

def is_valid(id):
    for r in ranges:
        if r[0] <= id <= r[1]:
            return True
    return False

### Part 1 ###
valid_count = 0
for id in ids:
    if is_valid(id):
        valid_count += 1
print(valid_count)

### Part 2 ###
ranges.sort(key=lambda x: x[0])
merged_ranges = ranges[:1]
for r in ranges[1:]:
    last = merged_ranges[-1]
    if r[0] <= last[1] + 1:
        merged_ranges[-1] = (last[0], max(last[1], r[1]))
    else:
        merged_ranges.append(r)

valid_count = 0
for range in merged_ranges:
    valid_count += range[1] - range[0] + 1

print(valid_count)
