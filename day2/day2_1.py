import re
class Set:
    def __init__(self, set_str):
        data = set_str.split(",")
        self.data = {}
        for d in data:
            info = d.strip().split(" ")
            self.data[info[1]] = int(info[0])
    def is_valid_set(self, valid_set):
        data = self.data
        return data.get("red", 0) <= valid_set[0] and data.get("green", 0) <= valid_set[1] and data.get("blue", 0) <= valid_set[2]
total = 0
with open("day2_input.txt") as file:
    for line in file:
        game_info = line.split(":")
        game_nums = re.findall(r'\d+', game_info[0])
        
        sets = game_info[1].split(";")
        game_valid = True
        for s in sets:
            game_valid = game_valid and Set(s).is_valid_set([12, 13, 14])
        total += int(game_nums[0]) if(game_valid) else 0
    print(total)       