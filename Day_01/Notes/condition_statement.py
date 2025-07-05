x = 1
y = 2
z = y>x

if y>x:
    print("Yes")

if z:
    print("Yes")

# python read part of condition base on indention
login_input = input("login: ")
if login_input == "Yes":
    print("Welcome")
    print("Back")

print("End")


# ELSE IF statement
if x == 1:
    print(x)
elif x == 2:
    print(x)
else:
    print(y)


color_input = input("Please enter a color: ")
match color_input:
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case "red":
        print("Stop")

# AND operator and OR operator
number = input("Enter Role: ")

if number == "admin" or number == "editor":
    print("Edit access enabled")
print("Edit not allowed")