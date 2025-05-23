class Player:
    def __init__(self,name, level):
        self._name  = name
        self._level = level
    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level

    @level.setter
    def setLevel(self, amount):
        self._level = amount
    
    @level.setter
    def addLevels(self, amount):
        self._level += amount

class PlayerInventory(Player):
    """The players inventory
    
        Atribute: 
        
        player  -> the player binded with the inventory

        data    -> the items inside of the inventory

        balance -> the money the player has
                
    """

    def __init__(self, name , level) -> None:
        super().__init__(name, level)
        self._data    = []
        self._balance = 0
        print(f"Le joueur {self._name} à été créer, il possède {self._data} et {self._balance} pièces d'or")

    @property
    def data(self) -> list:
        return self._data
    
    @property
    def balance(self) -> int:
        return self._balance
    
    @data.setter
    def addData(self, item) -> None:
        self._data.append(item)

    @balance.setter
    def addBalance(self, amount):
        self._balance += amount
    
    @property
    def getAllStats(self):
        return (f"Name:{self._name}\nLevel:{self._level}\nBalance:{self._balance}\nInventory:{self._data}")
        

player_1 = PlayerInventory("chamawel",0)
print(player_1.getAllStats)




