import csv

data = [
['Name', 'Age', 'Occupation'],
	['Alice', 30, 'Engineer'],
	['Bob', 25, 'Designer'],
]

with open('people.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerows(data)
