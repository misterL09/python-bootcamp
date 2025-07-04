x = 10
def function():
	print("Inner", x)

print("Outer", x)
function()
print("Outer", x)