coordinates = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            coordinates.append(f"{x} {y} {z}")
print(coordinates)

# List comprehension
coordinates = [
	f"{x} {y} {z}"
    for x in range(10)
    for y in range(10)
    for z in range(10)
]
print(coordinates)

