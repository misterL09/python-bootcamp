class Wallet:
    def __init__(self, initial_amount = 0):
        self.amount = initial_amount

food_wallet = Wallet(250)
print("Food Budget:", food_wallet.amount)
food_wallet.amount += 100
print("Food Budget:", food_wallet.amount)