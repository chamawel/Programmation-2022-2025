from inventory_obj import Inventory

class Chest(Inventory):
    def __init__(self, treasure : list, gold : int = 0):
        super().__init__(treasure, gold)
        if len(treasure) == 0:
            self._isempty = True
        else:
            self._isempty = False
    
    @property
    def isempty(self) -> bool:
        return self._isempty
    
    @isempty.setter
    def isempty(self,value : int):
        self._isempty = value 
    