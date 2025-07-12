from abc import ABC, abstractmethod

class Character(ABC):
    """Template or guideline for specific characters"""
    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense
    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class Knight(Character):
    """special character focus on defense"""
    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage

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

class Warrior(Character):
    def __init__(self, health, defense, strength=10 ):
        super().__init__(health, defense)
        self.strength = strength
    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage

enemy = Knight()
mage = Mage(10,10,5)
mage.attack(enemy)
print(enemy.health)

