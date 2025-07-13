from .character import Character

class Warrior(Character):
    def __init__(self, health, defense, strength=10 ):
        super().__init__(health, defense)
        self.strength = strength
    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage