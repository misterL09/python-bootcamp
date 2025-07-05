import csv

data = [
	{'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
	{'Name': 'Bob', 'Age': 25, 'Occupation': 'Designer'},
]

with open('people.csv', 'w', newline='') as file:
	writer = csv.DictWriter(file, fieldnames=data[0].keys())
	writer.writeheader()
	writer.writerows(data)
