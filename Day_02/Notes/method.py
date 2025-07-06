example = [1,3,3,5,4]
example.append(99)
print(example)

example.remove(4)
print(example)

other_example = [999,-1,0]
example.extend(other_example)
print(example)

example.insert(0,999)
print(example)

print(example.index(3))

print(example.count(999))

print(example)
example.pop(0)
print(example)

print(example.pop(-1))