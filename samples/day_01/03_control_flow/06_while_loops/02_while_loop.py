running = True

while running:
    choice = input("Provide command: ")
    if choice == "command 1":
        print("command 1 done")
    elif choice == "command 2":
        print("command 2 done")
    elif choice == "command 3":
        print("command 3 done")
    elif choice == "exit":
        running = False
