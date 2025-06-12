from player_obj import Player
from chest_obj  import Chest

chest1  = Chest(["banana","Bowling Ball"],3)
player1 = Player("chamawel")

print(player1.allData)
print(player1.allStats)

player1.takeDamage = 10

print(f"Contenus de chest1:\n{chest1.data}\n{chest1.balance} gold\n")

player1.levelUp = 3
player1.openChest(chest1)


print(player1.allData)
print(player1.allStats)
print(f"Contenus de chest1:\n{chest1.data}\n{chest1.balance} gold\n")

player1.openChest(chest1)