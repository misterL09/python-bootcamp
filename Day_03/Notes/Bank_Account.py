class BankAccount:
    def __init__(self,amount=0):
        self._balance = amount

    def deposit(self,amount):
        self._balance += amount

    def withdraw(self,amount):
        self._balance -= amount

    def printbalance(self):
        return self._balance

x = BankAccount(50)
print("deposit: ",x.deposit(100))
print("balance: ",x.printbalance())
print("withdraw: ",x.withdraw(20))
print("balance: ",x.printbalance())
