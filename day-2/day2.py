import re

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

def part_1():
    result = 0

    with open('input.txt', 'r') as file:
        for line in file:
            id = int(re.findall(r'(?<=Game )\d*', line)[0])

            line = re.sub(r'.*:', '', line)
            line = re.sub(r'\n', '', line)

            invalid_game = None
            
            games = line.split(';')

            for game in games:
                sets = game.split(',')

                for set in sets:
                    count = int(re.sub(r'[A-za-z]*', '', set))
                    color = (re.sub(r'\d* ', '', set)[0])
                    
                    if color == 'r':
                        if count > RED_CUBES:
                            invalid_game = True
                            break
                    if color == 'b':
                        if count > BLUE_CUBES:
                            invalid_game = True
                            break
                    if color == 'g':
                        if count > GREEN_CUBES:
                            invalid_game = True
                            break
                
            if invalid_game:
                #print(f'Game {id} is invalid')
                continue
            else:
                #print(f'Game {id} is valid.')
                result += id
    return result

#print(f'Part 1 result: {part_1()}')

def part_2():
    result = 0

    with open('input.txt', 'r') as file:
        for line in file:

            line = re.sub(r'.*:', '', line)
            line = re.sub(r'\n', '', line)
            
            games = line.split(';')

            min_red = 0
            min_green = 0
            min_blue = 0

            for game in games:
                sets = game.split(',')          

                for set in sets:
                    count = int(re.sub(r'[A-za-z]*', '', set))
                    color = (re.sub(r'\d* ', '', set)[0])
                    if color == 'r' and count > min_red:
                        min_red = count
                    if color == 'b' and count > min_blue:
                        min_blue = count
                    if color == 'g' and count > min_green:
                        min_green = count       

            game_power = (min_red * min_blue * min_green)
            result += game_power
    return result

print(part_2())