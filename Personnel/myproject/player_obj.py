class Player():
    def __init__(self,name : str, level : int, dmg : int, defence : int) -> None:
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
        """Adds x amount of level to a player and Boosts his stats"""
        self._level += amount
        
        self._dmg       += (1.5 * self._level)
        self._defence   += (1.2 * self._level)

        return f"Player {self._name} is now level {self.level} his/her stats have gone up!"
    
    @property
    def allStats(self) -> str:
        return f"Level:{self._level}\nDamage: {self._dmg}\nDefence:{self._defence}"


