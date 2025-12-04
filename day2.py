with open("day2.txt") as f:
    lines = f.readlines()[0].strip()

ranges = [range.split("-") for range in lines.split(",")]

### Part 1 ###
result = 0
for lower_range, higher_range in ranges:
    for num in range(int(lower_range), int(higher_range) + 1):
        first_half = str(num)[:len(str(num))//2]
        second_half = str(num)[len(str(num))//2:]
        if first_half == second_half:
            result += int(f"{first_half}{second_half}")

print(result)

### Part 1 ###
result = 0
for lower_range, higher_range in ranges:
    for num in range(int(lower_range), int(higher_range) + 1):
        for i in range(1, len(str(num))//2 + 1):
            if str(num) == str(num)[:i]*(len(str(num))//i):
                result += num
                break

print(result)
