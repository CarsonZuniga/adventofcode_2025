with open("day3.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def get_max_number(line, length):
    max_num = str(line[-length:])
    for i in range(len(line) - length - 1, -1, -1):
        candidate = line[i]
        batch_max = "0"
        for j in range(len(max_num)-1, -1, -1):
            candidate_max = f"{candidate}{max_num[:j]}{max_num[j+1:]}"
            if int(candidate_max) > int(batch_max):
                batch_max = candidate_max
        
        if int(batch_max) > int(max_num):
            max_num = batch_max

    return int(max_num)

### Part 1 ###
result = 0

for line in lines:
    max_num = get_max_number(line, 2)
    result += max_num

print(result)

### Part 2 ###
result = 0
for line in lines:
    max_num = get_max_number(line, 12)
    result += max_num

print(result)
