import re
class Game:
    def __init__(self):
        self.data = {}
    def add_set(self, set_str):
        data = set_str.split(",")
        for d in data:
            info = d.strip().split(" ")
            if(self.data.get(info[1], 0) < int(info[0])):
                self.data[info[1]] = int(info[0])
    def get_power(self):
        total = 1
        for i in self.data.values():
            total *= i
        return total
total = 0
with open("day2_input.txt") as file:
    for line in file:
        game_info = line.split(":")
        game_nums = re.findall(r'\d+', game_info[0])
        sets = game_info[1].split(";")
        game = Game()
        for s in sets:
            game.add_set(s)
        power = game.get_power()
        total += power
    print(total)       