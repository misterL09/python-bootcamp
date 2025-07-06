number = input("Enter number: ")
try:
    number_converted = int(number)
except ValueError:
    print("Invalid input. Please provide a valid integer")

start_process = False
while not start_process:
    if number < 0:
        print("Invalid input. Please provide a positive integer")
        start_process = True
    else:
        break