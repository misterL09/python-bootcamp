limit = int(input("Enter number: "))
for x in range(limit):
    print(x)

start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for x in range(start, end):
    print(x)

for x in range(start, end + 1):
    print(x)

for x in range(start, end, 2):
    print(x)