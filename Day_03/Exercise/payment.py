class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount > 0
#sample of no inheritance mano-mano ito
# class Coupon:
#     def __init__(self,amount,expired):
#         self.amount = amount
#         self.expired = expired
#     def valid(self):
#         return not self.expired and self.amount > 0

#sample of inheritance
class Coupon(Payment):
    def __init__(self, amount, expired):
        super().__init__(amount)
        self.expired = expired

    def valid(self):
        return super().valid() and not self.expired

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    def valid(self):
        is16digit = len(str(self.card_number)) >= 16
        return super().valid() and is16digit

class OnlinePayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    def valid(self):
        isGmail = str(self.email).endswith("@gmail.com")
        return super().valid() and isGmail


payment = Payment(1000)
coupon = Coupon(payment.amount,False)
card_payment = CardPayment(payment.amount,"AABBCC1234567890")
online_payment = OnlinePayment(payment.amount,"nathan@gmail.com")
print(payment.valid())
print(coupon.valid())
print(card_payment.valid())
print(online_payment.valid())