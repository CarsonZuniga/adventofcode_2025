with open("day3.txt") as f:
    lines = [line.strip() for line in f.readlines()]

### Part 1 ###
result = 0

for line in lines:
    max_num = str(line[-2:])
    for i in range(len(line) - 3, -1, -1):
        left_digit = max_num[0]
        right_digit = max_num[1]
        candidate = line[i]
        if int(left_digit) >= int(right_digit):
            candidate_max = f"{candidate}{left_digit}"
            if int(candidate_max) > int(max_num):
                max_num = candidate_max
        elif int(right_digit) > int(left_digit):
            candidate_max = f"{candidate}{right_digit}"
            if int(candidate_max) > int(max_num):
                max_num = candidate_max
    
    result += int(max_num)

print(result)
