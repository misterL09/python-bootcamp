class Paper:
    def __init__(self, contents):
        self.contents = contents

class Pen:
    def __init__(self, brand, color, capped=True, ink_level=1_000):
        self.brand = brand
        self.color = color
        self.capped = capped
        self.ink_level = ink_level

    def cap(self):
        self.capped = True

    def uncap(self):
        self.capped = False

    def refill(self, amount):
        self.ink_level += amount

    def write(self, paper, text):
        if self.capped:
            raise ValueError("Can't write when capped")

        if self.ink_level <= 0:
            raise ValueError("Not enough ink")

        if len(text) > self.ink_level:
            print("Low Ink: Will not be able to write everything")

        # Limit writing to available link
        paper.contents += text[:self.ink_level]

