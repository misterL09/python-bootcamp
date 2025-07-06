#you can use this as subtitution for using long if statement
country_code = {
    "PH": "Philippines",
    "US": "United States",
}
print(country_code["US"])

student_records ={
    "Juan": 70,
    "Maria": 98,
    "Joseph": 81,
    "Elise": 80
}
for student in student_records.keys():
    print(student)

wishlist = [
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
for index, order in enumerate(wishlist,start = 1):
    print(f"Item:{index}")
    for key,value in order.items():
        print(f"{key}:{value}")
