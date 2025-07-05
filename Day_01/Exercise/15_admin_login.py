correct_username = "admin"
correct_password = "admin"

username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

correct_given_input = username_input == correct_username and password_input == correct_password;
match correct_given_input:
    case True:
        print("Access Granted")
    case _ :
        print("Access Denied")