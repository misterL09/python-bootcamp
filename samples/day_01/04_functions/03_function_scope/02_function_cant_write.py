x = 10
def function():
    x = 5
    print("Inner", x)

print("Outer", x)
function()
print("Outer", x)
