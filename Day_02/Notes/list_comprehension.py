#original
example_list = []
for num in range(11):
    if num % 2 == 0:
        example_list.append(num)
print(example_list)

#using list comprehension
example_list2 = [num for num in range(11) if num % 2 == 0]
print(example_list2)


requests = {"Andrew": 10, "Peddy": 21, "Alex": 30}
banned = {"Alex"}
adults = [name for name, age in requests.items() if age >= 18]
print(adults)
allowed = [name for name in adults if name not in banned]
print(allowed)

ranks =""