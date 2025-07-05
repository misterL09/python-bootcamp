count = 0
stop_program = False
while not stop_program:
    choice = input("Provide command: ")
    match choice:
        case "add":
            count += 1
            print(count)
        case "sub":
            count -= 1
            print(count)
        case "double":
            count *= 2
            print(count)
        case "exit" | "Exit" | "EXIT":
            stop_program = True

    # if choice  == "add":
    #     count += 1
    #     print(count)
    # elif choice  == "sub":
    #     count -= 1
    #     print(count)
    # elif choice  == "double":
    #     count *= 2
    #     print(count)
    # elif choice  == "exit" or choice  == "EXIT":
    #     stop_program = True