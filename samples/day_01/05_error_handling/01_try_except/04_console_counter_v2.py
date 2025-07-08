"""Catch the KeyboardInterrupt error"""

count = 0
running = True

while running:
    choice = input("Provide command: ")

    # If choice equals add, increase count

    # Elif choice equals sub, decrease count

    # Elif choice equals double, double count

    if choice == "exit":
        running = False