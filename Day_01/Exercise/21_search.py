items = ["rice","noodles","toyo","spam","coffee"]
item_to_find = "spam"

for item in items:
    if item == item_to_find:
        print("found:", item)
        break
    else:
        print("not yet found")


