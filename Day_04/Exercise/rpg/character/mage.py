from .character import Character

class Mage(Character):
    def __init__(self, health, defense, magic=10 ):
        super().__init__(health, defense)
        self.magic = magic
    def attack(self, other):
        if other.defense > self.magic:
            damage = other.defense - self.magic
        else:
            damage = self.magic - other.defense
        other.health -= damage