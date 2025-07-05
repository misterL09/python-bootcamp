def greet(username, message):
    print(f"Hello {username}, {message}!")

greet("nathan","good day to you!")

# using default value in parameter
def greet2(username, message = "good day to you!"):
    print(f"Hello {username}, {message}!")

greet2("nathan")
greet("Kevin","welcome snake")