class NotNumber(ValueError):
    pass
class NotPositive(ValueError):
    def __init__(self):
        super().__init__("This is not Positive")
class NotWithinRange(ValueError):
    pass

number = input("Enter positive number [1,100]")

if not number.isnumeric() and not number[1:].isnumeric():
    raise NotNumber("This is not a number")

if int(number) < 0:
    raise NotPositive

if not( 1 <= int(number) <= 100):
    raise NotWithinRange