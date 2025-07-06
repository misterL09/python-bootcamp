# Ask the user for an input
email_input = input("Enter your email address: ")
# If valid gmail address
if email_input.endswith('@gmail.com'):
    print("This is a valid gmail address")
else:
    print("This is NOT a valid gmail address")