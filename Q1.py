"""
Question: Shopping Cart
1. Create a class named CartItem to represent items in the cart. Include attributes like name,
price, quantity, and a method calculate_item_price().
2. Create subclasses for different item types, e.g., ElectronicsItem and ClothingItem etc.
Override the calculate_item_price() method in each subclass.
3. Establish a class named ShoppingCart to represent the cart. Include an attribute items
(a list) to store added items. Implement methods add_item(), remove_item(), and show_cart().
4. Inside the ShoppingCart class, implement a method calculate_total_price() to sum the prices
of all items in the cart.
5. Instantiate objects of various item subclasses. Add these items to a ShoppingCart instance
using add_item(). Call calculate_total_price() on the cart to show the total price.
6. Create instances of items and the cart. Add items to the cart. Calculate and display the
total cart price using calculate_total_price().
"""

class CartItem:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_item_price(self):
        return self.price * self.quantity

class ElectronicsItem(CartItem):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def calculate_item_price(self):
        return self.price * self.quantity * 2

class ClothingItem(CartItem):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def calculate_item_price(self):
        return self.price * self.quantity * 3

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_cart(self):
        for item in self.items:
            print(item.name, item.price, item.quantity)

    def calculate_total_price(self):
        total=0
        for item in self.items:
            total+=item.calculate_item_price()
        return total

television = ElectronicsItem("Samsung Television", 1000, 2)
shirt = ClothingItem("Nike Shirt", 150, 3)

cart = ShoppingCart()

cart.add_item(television)
cart.add_item(shirt)

cart.show_cart()
print()
print("Total Price:", cart.calculate_total_price())
