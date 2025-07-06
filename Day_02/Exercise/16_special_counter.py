string = input('Enter string: ')
special_count = 0
special_char = '!@#$%^&*()'

for char in string:
    if char in special_char:
        special_count += 1
# Add one to special_count for each special char in string

print(special_count)