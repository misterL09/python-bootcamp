item_count = int(input("Enter item count: "))
total = 0

for item in range(item_count):
    item_price = int(input("Enter item price: "))
    item_qty = int(input("Enter item qty: "))
    total += item_price * item_qty
print(float(total))



# item_1_price = float(input("Input your item price 1: "))
# item_1_qty = int(input("Input your Price 1 Quantity: "))
# item_2_price = float(input("Input your item price 2: "))
# item_2_qty = int(input("Input your Price 2 Quantity: "))
# item_3_price = float(input("Input your item price 3: "))
# item_3_qty = int(input("Input your Price 3 Quantity: "))
#
# subtotal1 = item_1_price * item_1_qty
# subtotal2 = item_2_price * item_2_qty
# subtotal3 = item_3_price * item_3_qty
#
# total = subtotal1 + subtotal2 + subtotal3
# print(total)