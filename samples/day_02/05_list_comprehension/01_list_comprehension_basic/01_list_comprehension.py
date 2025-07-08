# Manual
numbers = [90, 100, 20, 10, 0]
double_numbers = []
for number in numbers:
    double_numbers.append(number * 2)
print(double_numbers)

# List comprehension
double_numbers = [number * 2 for number in numbers]
print(double_numbers)