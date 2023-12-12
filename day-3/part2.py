import re

result = 0
input = []
output = []
number_indices = []
symbols = '@#$%&*-+=/'

with open('input.txt', 'r') as file:
    for line in file:
        line = re.sub(r'\n', '', line)
        
        match = [m.span() for m in re.finditer(r'\d*', line)]
        temp = []

        input.append(line)

        for group in match:
            if group[1] - group[0] == 0:
                continue
            else:
                temp.append(group)
                
        number_indices.append(temp)

total = 0

def get_number(list, pair):
    number = ''
    for i in range(pair[0], pair[1]):
        number += list[i]
    return int(number)

for i in range(len(input)): #go through each row
    print(f"Row {i}:")
    for j in range (len(input[i])):
        number_matches = []
        if input[i][j] == "*":
            
            for k in range(j - 1 if j > 0 else j, j + 2 if j < len(input[i]) - 1 else j + 1):
                if i != 0:
                    if input[i - 1][k].isdigit():
                        print(f'row {i}: hit - row above')
                        print(number_indices[i - 1])
                        for pair in number_indices[i - 1]:
                            if k in range(pair[0],pair[1]):
                                number = get_number(input[i - 1], pair)
                                if number not in number_matches:
                                    number_matches.append(number)
                if input[i][k].isdigit():
                    print(f'row {i}: hit')
                    print(number_indices[i])
                    for pair in number_indices[i]:
                        if k in range(pair[0],pair[1]):
                            number = get_number(input[i], pair)
                            if number not in number_matches:
                                number_matches.append(number)
                if i != len(input) - 1:
                    if input[i + 1][k].isdigit():
                        print(f'row {i}: hit - row below')
                        print(number_indices[i + 1])
                        for pair in number_indices[i + 1]:
                            if k in range(pair[0],pair[1]):
                                number = get_number(input[i + 1], pair)
                                if number not in number_matches:
                                    number_matches.append(number)
                print(number_matches)
        if len(number_matches) == 2:
            ratio = number_matches[0] * number_matches[1]
            total += ratio            
        
print(f"The sum is {total}.")
