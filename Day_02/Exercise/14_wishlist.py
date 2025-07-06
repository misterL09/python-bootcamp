item = [
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
},
]
for index, order in enumerate(item,start = 1):
    print(f"Item:{index}")
    for key,value in order.items():
        print(f"\t{key}:{value}")
    print()

