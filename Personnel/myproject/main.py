from player_obj import Player
from chest_obj  import Chest

chest1  = Chest(["banana","Bowling Ball"],3)
player1 = Player("chamawel")

player1.levelUp = 3

print(player1.allData)

print(player1.openChest(chest1))
print(player1.allData)