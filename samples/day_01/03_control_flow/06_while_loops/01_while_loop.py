correct_password = "pass"
password = input("Enter password: ")
while password != correct_password:
    password = input("Enter password: ")

print("Trying alternate version: ")

# Alternative version
correct_password = "pass"
password = ""
while password != correct_password:
    password = input("Enter password: ")

