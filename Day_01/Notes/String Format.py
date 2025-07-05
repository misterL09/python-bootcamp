# curly bracket is placeholder
message = "Hello {}! Nice to meet you!"
print(message)

formatted_message = message.format("Nathan")
print(formatted_message)


message = "Hello {}. Your nickname is {}"
name = input("Enter name: ")
nickname = input("Enter nickname: ")

formatted_message = message.format(name, nickname)
print(formatted_message)

# string formatting modern
name = input("enter your name:")
print(f"Hello {name}, nice meeting you!")
