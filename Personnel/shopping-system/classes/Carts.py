class Cart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, quantity=1, price=0.0):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] -= quantity
            if self.items[item_name]['quantity'] <= 0:
                del self.items[item_name]
    
    def get_total(self):
        return sum(info['quantity'] * info['price'] for info in self.items.values())

    def clear(self):
        self.items.clear()

    def list_items(self):
        return [
            {'item': name, 'quantity': info['quantity'], 'price': info['price']}
            for name, info in self.items.items()
        ]