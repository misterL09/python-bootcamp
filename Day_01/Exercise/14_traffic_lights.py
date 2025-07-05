color_input = input("Please enter a color: ")
match color_input:
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case "red":
        print("Stop")
    case _:
        print("not part of condition")


# if color_input == "green":
#     print("Go")
# elif color_input == "yellow":
#     print("Wait")
# elif color_input == "red":
#     print("stop")
# else:
#     print("not part of condition")
