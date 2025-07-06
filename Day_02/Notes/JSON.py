import json

data = [
{
'Name': 'Smartphone',
'Info': 'Latest model smartphone',
'Price': 70_000.00,
'Stock': 25
},
{
'Name': 'Wireless Headphones',
'Info': 'Noise-canceling headphones',
'Price': 10_000.00,
'Stock': 50
}
]
with open('people.json', 'w') as file:
    json.dump(data, file, indent = 4)

