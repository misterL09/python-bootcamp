try:
    user_input = int(input("Enter Number: "))
    result = 5 / user_input
except ValueError:
    print("Input is not a valid number")
except ZeroDivisionError:
    print("Number is a zero!")
except KeyboardInterrupt:
    print("You stopped the code prematurely!")
