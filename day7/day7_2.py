from collections import Counter

class PokerHand:
    def __init__(self, hand, bet):
        self.hand = hand
        self.bet = int(bet)
        frequency = Counter(hand)
        self.set_frequency(frequency)
        
    def set_frequency(self, frequency):
        joker_frequency = frequency['J']
        if(joker_frequency < 5):
            most_common = frequency.most_common(5)
            for common in most_common:
                if(common[0] != 'J'):
                    frequency[common[0]] = common[1] + joker_frequency
            del frequency['J']
        self.frequency = frequency
        
    def __str__(self):
        return f'{self.hand} {self.bet} {self.frequency}'
    
    def compare(self, other_hand):
        self_most_freq = self.frequency.most_common(5)
        other_most_freq = other_hand.frequency.most_common(5)
        if(len(self_most_freq) > len(other_most_freq)):
            return 1
        elif(len(self_most_freq) < len(other_most_freq)):
            return -1
        elif(len(self_most_freq) == len(other_most_freq)):
            if(self_most_freq[0][1] < other_most_freq[0][1]):
                return 1
            elif(self_most_freq[0][1] > other_most_freq[0][1]):
                return -1
            else:
                lookup = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7':7, '6':6,'5':5,'4':4,'3':3,'2':2}
                for i in range(len(self.hand)):
                    self_val = lookup[self.hand[i]]
                    other_val = lookup[other_hand.hand[i]]
                    if (self_val < other_val):
                        return 1
                    elif(self_val > other_val):
                        return -1
        return 0

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while(j > 0 and arr[j-1].compare(arr[j]) < 0 ):
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j = j - 1            
    
with open("day7_input.txt") as file:
    lines = file.readlines()
    arr = []
    for line in lines:
        data = line.split(" ")
        p = PokerHand(data[0], data[1])
        arr.append(p)
    insertion_sort(arr)
    total = 0
    for i in range(len(arr)):
        total += (i + 1) * arr[i].bet
    print(total)