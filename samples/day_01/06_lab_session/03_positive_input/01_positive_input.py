# Ask the user for an input that should be a number
number = input("Enter number: ")

# Then try to convert this into an integer using the following:
number_converted = int(number)

"""
Base Exercise:
But this will cause an error if the user gives a non-integer input. 
Can you make the error print the following if the input is invalid?
"""

"""
# Challenge: Positive Integer
Next, the input should be a POSITIVE integer (greater or equal to zero). 
If the input is not, print this message instead:
    Invalid input. Please provide a positive integer
"""

"""
# Challenge: Continuous Positive Integer
Finally, keep asking the user for input for as long as they do not give a valid, positive, integer
    Enter number: "Invalid Input 1"
    Enter number: "Invalid Input 2"
    ...
"""