import re

# Number of cards input. The program relies on knowing this beforehand.
NUM_OF_CARDS = 212
input = 'input.txt'

cards = [1] * NUM_OF_CARDS

with open(input, 'r') as file:

    lines = file.readlines()
    for i, line in enumerate(lines):

        line = re.sub(r'(^.*:|\n)', '', line) 
        line = line.split('|')
        winning_cards = []
        played_cards = []
        cards_won = 0

        for match in re.findall(r'\d*', line[0]):
            if len(match) > 0:
                winning_cards.append(match)
        for match in re.findall(r'\d*', line[1]):
            if len(match) > 0:
                played_cards.append(match)
            
        for number in played_cards:
            if number in winning_cards:
                cards_won += 1

        for j in range(cards[i], 0, -1): # for each copy        
            for k in range(cards_won, 0, -1): # for each winning card
                cards[i + k] += 1
                
total = 0
for copies in cards:
    total += copies

print(f'Total: {total}')
        