class Shop:
    def __init__(self, inventory):
        """
        inventory: dict mapping item names to stock counts, e.g. {'apple': 10, 'banana': 5}
        """
        self.inventory = inventory

    def take_item(self, item_name, quantity=1):
        """
        Takes 'quantity' units of the specified item from the shop.
        Returns the item name as a string if enough stock is available, else raises a ValueError.
        """
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            return item_name
        raise ValueError(f"Not enough '{item_name}' in stock (requested: {quantity}, available: {self.inventory.get(item_name, 0)})")