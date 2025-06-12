from Carts import Cart

class Customer(Cart):
    def __init__(self, name, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email}, cart_items={self.items})"