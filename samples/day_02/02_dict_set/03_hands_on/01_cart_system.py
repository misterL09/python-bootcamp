cart = []

def add(cart, name, price, quantity):
	"""Add a new item with the following details"""

def remove(cart, index):
	"""Remove entry with key name from cart"""


def show_all(cart):
	"""Print all contents in cart"""

def show_total(cart):
	"""Calculate and print total of cart"""

# Test

print("Adding items...")
add(cart, "Taho", 10, 3)
add(cart, "Isaw", 10, 5)
add(cart, "Kwek-kwek", 8, 4)
show_all(cart)

print("Removing item at index 1 (Isaw)...")
remove(cart, 1)
show_all(cart)

print("Showing total...")
show_all(cart)