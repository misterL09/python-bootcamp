ranks =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
ranks[-4] = "Drawn"
ranks[-3] = "Drawn"
ranks[-2] = "Drawn"
ranks[-1] = "Drawn"
ranks[0] = "Drawn"
print(ranks)

ranks =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
count = 0
for item in ranks:
    if item == '10' or item == 'J' or item == 'Q' or item == 'K' or item == 'A':
        ranks[count] = "Drawn"
    count += 1
print(ranks)