with open("day1.txt") as f:
    lines = f.readlines()

### Part 1 ###

result = 0
count = 50

for line in lines:
    if line[0] == "L":
        count -= int(line[1:])
    elif line[0] == "R":
        count += int(line[1:])

    count = count % 100
    if count == 0:
        result += 1

print(result)

### Part 2 ###

result = 0
count = 50

for line in lines:
    rotations = 0
    if line[0] == "L":
        count -= int(line[1:])
        if count < 0:
            if count + int(line[1:]) != 0:
                rotations = int(abs(count) / 100) + 1
            else:
                rotations = int(abs(count) / 100)
        if count == 0:
            rotations = int(abs(count) / 100) + 1

    elif line[0] == "R":
        count += int(line[1:])
        if count > 99:
            rotations = int(count / 100)
    
    count = count % 100
    result += abs(rotations)

print(result)