number = input("Enter Role: ")
match number:
    case "admin" | "editor":
        print("Edit access enabled")
    case _ :
        print("Edit not allowed")

# if number == "admin" or number == "editor":
#     print("Edit access enabled")
# print("Edit not allowed")