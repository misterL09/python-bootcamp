count = 0
running = True
while running:
    choice = input("Provide command: ")

    # If choice equals add, increase count
    # elif choice equals sub, decrease count
    # elif choice equals double, double count
    if choice == "exit":
        running = False
