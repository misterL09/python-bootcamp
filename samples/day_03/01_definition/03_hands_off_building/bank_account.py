class BankAccount:

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough money")

        self.balance -= amount

    def deposit(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough money")

        self.balance += amount