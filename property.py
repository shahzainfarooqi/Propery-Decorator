class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)
print(p.price)      # Getter
p.price = 150       # Setter
print(p.price)
del p.price         # Deleter

# Trying to access after deletion will raise an AttributeError
# print(p.price)    # Uncommenting this will raise an error
