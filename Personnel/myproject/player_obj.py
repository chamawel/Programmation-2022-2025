from inventory_obj import Inventory

class Player(Inventory):
    """Player Object:\n
        Inherite the Inventory\n
        ATRIBUTES + BASE STATS\n
        name  : str (must be set)\n
        level : int = 0\n
        dmg   : int = 1\n
        defence : int  = 1\n
        items   : list = []\n
        balance : int  = 0\n

    """
    def __init__(self,name : str, level : int = 0, dmg : int = 1, defence : int = 1, items : list = [], balance : int = 0) -> None:
        super().__init__(items,balance)
        self._name       = name
        self._level      = level
        self._dmg        = dmg
        self._defence    = defence

    @property
    def level(self)     -> int:
        """Level of the player"""
        return self._level

    @property
    def dmg(self)       -> int:
        """damage of the player"""
        return self.dmg

    @property
    def defense(self)   -> int:
        """defence of the player"""
        return self._defence


    @level.setter
    def levelUp(self,amount : int) -> str:
        """Adds {amount} of level to a player and Boosts his stats"""
        self._level += amount
        
        self._dmg       += (1.5 * self._level)
        self._defence   += (1.2 * self._level)

        return f"Player {self._name} is now level {self.level} his/her stats have gone up!"
    
    @property
    def allStats(self) -> str:
        """ Returns all of the player's stats\n
            Level,damage and defence
        """
        return f"{self._name}'s stats:\nLevel:{self._level}\nDamage: {self._dmg}\nDefence:{self._defence}"
    
    @property
    def allData(self) -> str:
        """Returns all of the player's data\n
           Items and Balance 
        """
        return f"{self._name}'s data:\nItems: {self._data}\nBalance:{self._balance}"


