import re

def get_winning_times(time, distance):
    total = 0
    for i in range(1, time):
        complement = i
        if(complement * (time - complement) > distance):
            total += 1
    return total
    
with open("day6_input.txt") as file:
    lines = file.readlines()
    times = re.findall(r'\d+',lines[0].split(":")[1])
    distances = re.findall(r'\d+',lines[1].split(":")[1])
    distance = int(''.join(distances))
    time = int(''.join(times))
    print(get_winning_times(time, distance))

        