coordinates = [
	(x, y, z)
    for x in range(10)
    for y in range(10)
    for z in range(10)
]
print(coordinates)

coordinates = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            coordinates.append((x, y, z))
print(coordinates)
