import re

def convert_to_map_value(num, arr):
    dest = int(arr[0])
    source = int(arr[1])
    r = int(arr[2]) - 1
    if(source <= num and  source + r >= num):
        diff = num - source
        return (dest + diff, True)
    return (num, False)

def convert_value_with_map(num, data):
    for d in data:
        vals = convert_to_map_value(num, d)
        if(vals[1]):
            return vals[0]
    return num

def get_location_for_seed(seed, all_maps):
    soil = convert_value_with_map(seed, all_maps["seed-to-soil"])
    fert = convert_value_with_map(soil,  all_maps['soil-to-fertilizer'])
    water = convert_value_with_map(fert,  all_maps['fertilizer-to-water'])
    light = convert_value_with_map(water,  all_maps['water-to-light'])
    temp = convert_value_with_map(light,  all_maps['light-to-temperature'])
    humid = convert_value_with_map(temp,  all_maps['temperature-to-humidity'])
    loc = convert_value_with_map(humid,  all_maps['humidity-to-location'])
    return loc
    
with open("day5_input.txt") as file:
    lines = file.readlines()
    seeds = re.findall(r'\d+',lines[0].split(":")[1])
    all_maps = {}
    curr_map = ""
    for i in range(1, len(lines)):
        line = lines[i]
        if("map" in line):
            curr_map = line.split(" ")[0]
        elif(len(line.strip()) == 0):
            continue
        else:
            map_data = all_maps.get(curr_map, [])
            map_data.append( re.findall(r'\d+', line))
            all_maps[curr_map] = map_data
            
    min_loc = 100000000000000000
    for s in seeds:
         loc = get_location_for_seed(int(s), all_maps)
         if(loc < min_loc):
             min_loc = loc
    print(min_loc)       