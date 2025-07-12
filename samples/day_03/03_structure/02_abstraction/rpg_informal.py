class Character:
    def __init__(self, health=10, defense=10):
        self._health = health
        self._defense = defense

    def attack(self, other):
        raise NotImplementedError()

class Knight(Character):
    pass

enemy = Character()
knight = Knight()

knight.attack(enemy)
