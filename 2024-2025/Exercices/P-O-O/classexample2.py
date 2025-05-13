class PlayerInventory:
    """The players inventory
    
        Atribute: 
        
        player  -> the player binded with the inventory

        data    -> the items inside of the inventory

        balance -> the money the player has
                
    """

    def __init__(self, player) -> None:
        self._player  = player
        self._data    = []
        self._balance = 0
        print(f"Le joueur {self._player} à été créer, il possède {self._data} et {self._balance} pièces d'or")

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


player_1 = PlayerInventory("chamawel")

