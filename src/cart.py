
class Cart(object):
    """A simple cart"""
    def __init__(self):
        self.items = []

    def add(self, name, quantity, price):
        self.items.append([name, quantity, price])

    def cost(self):
        amount = 0.0
        for name, quantity, price in self.items:
            amount += quantity * price
        return amount
