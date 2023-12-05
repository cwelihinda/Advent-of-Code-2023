import re
class Card:
    def __init__(self, line):
        card_data = line.split(":")
        card_numbers = card_data[1].split("|")
        self.winning_numbers = re.findall(r'\d+', card_numbers[0])
        self.numbers = re.findall(r'\d+', card_numbers[1])
    def get_winners(self):
        winners = []
        for i in self.numbers:
            if(i in self.winning_numbers):
                winners.append(i)
        return winners
    
    
with open("day4_input.txt") as file:
    lines = file.readlines()
    total = 0
    for i in lines:
        card = Card(i)
        num_winners = len(card.get_winners())
        if(num_winners > 0):
            total += 2 ** (num_winners - 1)
    print(total)