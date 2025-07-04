x = 10
def function(x):
    print("Inner", x)
    x = 5
    print("Inner", x)

print("Outer", x)
function(3)
print("Outer", x)
