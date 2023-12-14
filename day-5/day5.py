'''
I goofed when parsing the input; two newlines need to be added to the end for
this code to work.
'''

import re

input = 'input.txt'

seeds = []


#def parse_map()

with open(input, 'r') as file:
    parse = 0
    lines = file.readlines()

    # Each map is stored as a list of tuples inside a larger 2-dimensional list.
    map_index = 0
    maps = []
    temp = []

    # Parse text file into list
    for i, line in enumerate(lines):
        if parse != 0:
            if line != '\n':
                map_values = tuple(int(x) for x in re.findall(r'\d*', line) if x)
                #maps.append(map_values)
                temp.append(map_values)
                continue
            else:
                parse = 0
                maps.append(temp)
                temp = []
                #print(maps)
                continue
        line = re.sub(r'\n', '', line)
    
        # Seed list
        if re.match(r'^seeds: ', line):
            for match in re.findall(r'\d*', line):
                if len(match) > 0:
                    seeds.append(int(match))
        
        # Mapping
        if re.match(r'(^seed|^soil|^fertilizer|^water|^light|^temperature|^humidity)', line):
            print(line)
            parse = i


# Conversion

parsed_output = [0] * len(seeds)
for num, seed in enumerate(seeds):
    parsed_output[num] = seed
    print(f'Initial seed: {seed}')
    for map in maps:
        print(f'Current seed value: {parsed_output[num]}')
        for i in range(len(map)):   
            if parsed_output[num] in range(map[i][1], map[i][1] + map[i][2]):
                print(map[i])
                offset = map[i][0] - map[i][1]
                parsed_output[num] = parsed_output[num] + offset
                print(f'Offset: {offset}')
                break # Skips after first map
            else:
                print(f'Skipping map {map[i]}, not in range')

    print(f'Step {num + 1}: {parsed_output}')


print(parsed_output)


parsed_output.sort()
print (parsed_output[0])