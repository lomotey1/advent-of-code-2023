import re
NUM_OF_CARDS = 212

cards = [1] * NUM_OF_CARDS

print(cards)

with open('input.txt', 'r') as file:

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
            

            for k in range(cards_won, 0, -1):
                cards[i + k] += 1


print(cards)
total = 0
for copies in cards:
    total += copies

print(total)
        




