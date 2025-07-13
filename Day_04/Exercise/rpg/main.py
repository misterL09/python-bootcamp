from character.knight import Knight
from character.warrior import Warrior
from character.mage import Mage

enemy = Knight()
mage = Mage(10,10,5)
mage.attack(enemy)
print(enemy.health)


# player = Knight(defense=30)
# enemy = Character()
# player.attack(enemy)
# print(enemy.health)