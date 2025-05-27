class Inventory:
    """ inventory
    
        Atribute: 

        data    -> the items inside of the inventory

        balance -> the money 'the Inventory Has'
                
    """

    def __init__(self, data : list , balance : int) -> None:
        self._data    = data
        self._balance = balance

    @property
    def data(self) -> list:
        return self._data
    
    @property
    def balance(self) -> int:
        return self._balance
    
    @data.setter
    def addDataToInventory(self, item) -> None:
        self._data.append(item)

    @balance.setter
    def addToBalance(self, amount):
        self._balance += amount