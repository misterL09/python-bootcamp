binary_h = list(bin(ord('h')))
binary_h = binary_h[2:]
print(binary_h)

binary_a = list(bin(ord('a')))
binary_a = binary_a[2:]

binary = 3*(binary_h +binary_a)
print(binary)
