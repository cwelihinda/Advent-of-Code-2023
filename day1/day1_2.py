import regex as re
def convert_to_num(num_str):
    numbers_lookup = {"one": 1,"two" : 2,"three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9}
    return numbers_lookup[num_str] if(len(num_str) > 1) else int(num_str)
total = 0
with open("day1_input.txt") as file:
    for line in file:
        nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        total += convert_to_num(nums[0]) * 10 + convert_to_num(nums[-1])
print(total)