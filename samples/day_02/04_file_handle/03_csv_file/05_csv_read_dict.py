import csv

with open('people.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
