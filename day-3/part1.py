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
    valid_numbers = []
    for idx, line in enumerate(number_indices): #each number
        for index, pair in enumerate(line): # each pair is the indices of a number to be considered
            for n in range(pair[0] if pair[0] == 0 else pair[0] - 1, pair[1] if pair[1] == len(input[index]) else pair[1] + 1): # expands for diagonals if necessary
        
                if input[i][n] in symbols:
                    if pair not in valid_numbers and pair in number_indices[i]:
                        valid_numbers.append(pair)

                if 0 <= i < len(input[index]) - 1:
                    if input[i + 1][n] in symbols:
                        if pair not in valid_numbers and pair in number_indices[i]:
                            valid_numbers.append(pair)
                
                if len(input[index]) - 1 >= i > 0:
                    if input[i - 1][n] in symbols:
                        if pair not in valid_numbers and pair in number_indices[i]:
                            valid_numbers.append(pair)

    print(f'vaid pairs for row {i}: {valid_numbers}')
    for number in valid_numbers:
        total += get_number(input[i], number)
        
print(f"The sum is {total}.")
