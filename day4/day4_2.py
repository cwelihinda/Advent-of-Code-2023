import re
class Card:
    def __init__(self, line):
        card_data = line.split(":")
        card_header = card_data[0]
        card_numbers = card_data[1].split("|")
        self.card_number = int(re.findall(r'\d+', card_header)[0])
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
    multipliers = {}
    for i in range(len(lines)):
        card = Card(lines[i])
        num_winners =  len(card.get_winners());
        upper_range = min(len(lines) + 1, card.card_number + num_winners + 1)
        multipliers[card.card_number] = multipliers.get(card.card_number, 0) + 1
        for j in range(multipliers.get(card.card_number, 0)):
            for winner in range(card.card_number + 1,upper_range, 1):
                multipliers[winner] = multipliers.get(winner, 0) + 1
        total += multipliers.get(card.card_number, 0)
    print(total)