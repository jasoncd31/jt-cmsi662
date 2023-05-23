# Shopping Cart Class thats SUPER secure in python3
# The shopping cart class must (1) have its own id, (2) hold the id of the customer that the cart belongs to, and (3) the items in the cart along with their quantities
# Provide a way for users to query the id, customerId, and items from the cart. Make sure that no one can change the cart indirectly by modifying the values you provided them (you may need to research “immutability” and “defensive copying”).
# Provide a way for users to add, update, and remove items.
# Ensure the id and customerId of the cart can NEVER be changed.
# Provide a method to get the total cost of the items in the cart.
# Shopping cart ids must be uuid4s. Find out how to generate them in the language of your choice.
# All customer ids must have the following form: 3 letters, 5 numbers, 2 letters, a dash, and finally an A or a Q. Always check for valid customer ids.
# Ensure you can never have a negative quantity for an item in the cart. Also put and upper bound on quantities as well (you should know why we need bounds like this, pretty much everywhere).
# Make sure items you add to the cart are in an “inventory.” Item names should also be length-bounded and the characters in the names restricted. Make sure any string content in your project is bounded as well.
# Employ immutability everywhere you possibly can.
# Throw exceptions where it makes sense to do so. Do not allow bad data to creep in, ever.

import uuid
import re

class Item():
    #Creates an item object to be placed in the shopping cart.
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.item_id = uuid.uuid4()
        self.item_name = re.compile(r'[a-zA-Z]{1,20}')

    @property
    def item_id(self):
        return self.item_id

    @property
    def item_name(self):
        return self.item_name

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = price

class ShoppingCart(object):
    #Creates shopping cart objects for users of our fine website.
    
    items_in_cart = {}

    def __init__(self, owner_of_cart):
        self.owner_of_cart = owner_of_cart
        self.cart_id = uuid.uuid4()
        self.customer_id = re.compile(r'[a-zA-Z]{3}\d{5}[a-zA-Z]{2}[-][A|Q]')

    @property
    def cart_id(self):
        return self.cart_id
    
    @property
    def customer_id(self):
        return self.customer_id

    def add_item(self, product, quantity):
        # Add product to the cart.
        # validate SKU
        # validate product is in catalog
        # validate quantity is greater than 0

        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added.")
        else:
            print (product + " is already in the cart.")

    def remove_item(self, product):
        # Remove product from the cart.
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print (product + " removed.")
        else:
            print (product + " is not in the cart.")
