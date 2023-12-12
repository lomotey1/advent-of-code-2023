import re

points = 0

'''
Returns scoring based on the number of cards won.
'''
def get_score(winning_cards):
    if winning_cards == 0: return 0
    score = 1
    for i in range (winning_cards + 1, 2, -1):
        score *= 2
    return score

with open('input.txt', 'r') as file:
    for line in file:
        winning_cards = []
        played_cards = []
        cards_won = 0
        line = re.sub(r'(^.*:|\n)', '', line)
        
        line = line.split('|')

        for match in re.findall(r'\d*', line[0]):
            if len(match) > 0:
                winning_cards.append(match)
        for match in re.findall(r'\d*', line[1]):
            if len(match) > 0:
                played_cards.append(match)
        
        for number in played_cards:
            if number in winning_cards:
                cards_won += 1

        points += get_score(cards_won)

print(f'Total points: {points}')


