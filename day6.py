import math

with open("day6.txt") as f:
    raw_lines = [line.rstrip("\n") for line in f]
lines = [line.split() for line in raw_lines]

### Part 1 ###
result = 0
for i in range(len(lines[0])):
    oper = lines[-1][i]
    operands = [int(lines[j][i]) for j in range(len(lines)-1)]
    if oper == "*":
        result += math.prod(operands)
    else:
        result += sum(operands)

print(result)

### Part 2 ###
result = 0
opers = lines[-1]
operands = []
for i in range(len(raw_lines[0])):
    if all(raw_lines[j][i] == " " for j in range(len(raw_lines)-1)):
        oper = opers.pop(0)
        if oper == "*":
            result += math.prod(operands)
        else:
            result += sum(operands)
        operands = []
    else:
        col_vals = []
        for j in range(len(raw_lines)-1):
            if raw_lines[j][i] != " ":
                col_vals.append(raw_lines[j][i])
        operands.append(int("".join(col_vals)))

# Handle final operands after loop ends
if operands:
    oper = opers.pop(0)
    if oper == "*":
        result += math.prod(operands)
    else:
        result += sum(operands)

print(result)
