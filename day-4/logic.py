def scoring(number):
    if number == 0: return 0
    score = 1
    for i in range (number + 1, 2, -1):
        score *= 2
    return score
print(scoring(4))