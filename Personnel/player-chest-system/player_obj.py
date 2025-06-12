from inventory_obj import Inventory
from chest_obj import Chest

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
    def __init__(self,name : str, level : int = 0,health : int = 100 , dmg : int = 1, defence : int = 1, items : list = [], balance : int = 0) -> None:
        super().__init__(items,balance)
        self._name       = name
        self._level      = level
        self._health     = health
        self._dmg        = dmg
        self._defence    = defence
    

    @property
    def level(self)     -> int:
        """Level of the player"""
        return self._level
    
    @property
    def health(self)    -> int:
        """Health Of The Player"""
        return self._health

    @property
    def dmg(self)       -> int:
        """damage of the player"""
        return self.dmg

    @property
    def defense(self)   -> int:
        """defence of the player"""
        return self._defence


    @level.setter
    def levelUp(self,amount : int) -> None:
        """Adds {amount} of level to a player and Boosts his stats"""
        self._level += amount
        
        self._dmg       += (1.5 * self._level)
        self._defence   += (1.2 * self._level)

        print(f"Player {self._name} is now level {self.level} his/her stats have gone up!\n")
    
    @health.setter
    def takeDamage(self,amount : int) -> None:
        """Deals 'amount' of damage to the player"""
        self._health -= amount
        if self._health <= 0:
            print(f"player {self._name} has died !!")
            del self

        print(f"{self._name} took {amount} of damage his/her health goes down to {self._health}")

    @property
    def allStats(self) -> str:
        """ Returns all of the player's stats\n
            Level,damage, defence and health
        """
        return f"{self._name}'s stats:\nLevel:{self._level}\nDamage: {self._dmg}\nDefence:{self._defence}\nHealth: {self._health}\n"
    
    @property
    def allData(self) -> str:
        """Returns all of the player's data\n
           Items and Balance 
        """
        return f"{self._name}'s data:\nItems: {self._data}\nBalance:{self._balance}\n"
    
    def openChest(self, chest : Chest) -> None:
        if chest.__class__ == Chest:
            if chest._isempty == False:
                self._data.extend(chest._data)
                self._balance += chest._balance
                
                msg = f"Successfully opened the chest the player got:\n{chest._data} and {chest._balance} gold\n"
                
                chest._data.clear()
                chest._balance = 0
                chest.isempty  = True
            else:
                msg = f"The Chest is empty\n"
        else:
            msg = f"Tried to open something other than a Chest\n"
        
        print(msg)


