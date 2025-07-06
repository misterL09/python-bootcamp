# Ask the user for an input
user_input = input("Enter number: ")
clean_input = user_input.lower().strip()
clean_input = clean_input.replace(',','')

if clean_input.isnumeric():
    # If user enters a valid number
    clean_input = int(clean_input)
    print(clean_input + 1)
else:
    print("Please enter a valid number!")