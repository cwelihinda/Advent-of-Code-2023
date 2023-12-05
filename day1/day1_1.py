import re
total = 0
with open("day1_input.txt") as file:
    for line in file:
        nums = re.findall(r'\d', line)
        total += int(nums[0]) * 10 + int(nums[-1])
print(total)