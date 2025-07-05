# correct_password = "admin"
# password = ""
# while password != correct_password:
#      password = input("Enter password: ")


stop_program = False
while not stop_program:
    choice = input("Provide command: ")
    if choice  == "1":
        print("command 1 done")
    elif choice  == "2":
        print("command 2 done")
    elif choice  == "3":
        print("command 3 done")
    elif choice  == "exit":
        stop_program = True