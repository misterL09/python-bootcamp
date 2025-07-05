letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
step = int(input("Enter the step: "))

sublist = letters[start:end:step]
print(sublist)

