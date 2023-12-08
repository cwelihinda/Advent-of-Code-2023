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
    curr_map = ""
    total = 1
    for i in range(len(times)):
        distance = int(distances[i])
        time = int(times[i])
        total *= get_winning_times(time, distance)
    print(total)
        