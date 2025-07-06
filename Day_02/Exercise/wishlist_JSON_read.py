import json

with open('people.json', 'r') as file:
    data = json.load(file)
print(data)

with open(r"C:\Users\User\PycharmProjects\python-bootcamp\Day_02\Exercise\people.json",'r') as file:
    data = json.load(file)
print(data)