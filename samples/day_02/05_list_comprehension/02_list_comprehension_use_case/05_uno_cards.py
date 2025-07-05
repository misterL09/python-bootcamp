colors = ["Red","Green","Blue","Yellow"]
values = ["1","2","3","4","5","6","7","8","9","R","S","+2"]

cards = [f"{c}-{v}" for c in colors for v in values]
cards.extend(["Color","Color","Color","Color"])
cards.extend(["+4","+4","+4","+4"])

print(cards)