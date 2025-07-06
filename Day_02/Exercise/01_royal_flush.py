ranks =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
for item in ranks[-4:]:
    print(item)
print(ranks[0])

print(*ranks[-4:],ranks[0])
print(*ranks[-4:],ranks[0],sep ='\n')

#skip counting
print(*ranks[::4])