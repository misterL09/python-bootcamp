def coffee_price(kind, size, has_discount):
    """
    Returns the final price with the following scheme:
        Base Price: Americano (100), Latte (110), Cappuccino (120)
        Size Multiplier: Small (x0.8), Medium  (x1.0), Large (x1.2)
        Has Discount: x0.88 (removed VAT)
    """
    return 0

print(coffee_price("Latte", "Large", True))
print(coffee_price("Americano", "Small", False))

