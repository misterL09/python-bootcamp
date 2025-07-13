from .character import Character

class Knight(Character):
    """special character focus on defense"""
    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage