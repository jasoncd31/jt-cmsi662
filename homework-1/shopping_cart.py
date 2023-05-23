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

def validate_customer_id(customer_id):
    valid_id = re.match(r'[a-zA-Z]{3}\d{5}[a-zA-Z]{2}[-][A|Q]', customer_id)
    if not valid_id:
        raise Exception("Not a valid customer id")
    return customer_id

class Item():
    #Creates an item object to be placed in the shopping cart.
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.item_id = uuid.uuid4()
        self.item_name = re.compile(r'[a-zA-Z]{1,20}')

    @property
    def item_id(self):
        return self.item_id.deepcopy()

    @property
    def item_name(self):
        return self.item_name.deepcopy()

    @property
    def price(self):
        return self.price.deepcopy()

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = price

class SKU(): 
    def validated(code): 
        # if code isn't a string, throw an error
        if type(code) != "str":
            raise TypeError("SKU must be a string.")
        # if code doesn't match the regex, throw an error
        if (re.match(r'[A-Z]{3}_[A-Z]{3}_\d{2}$', code)):
            raise TypeError("SKU improperly formatted.")
            
        return code
    def __init__(self, code):
        code = validated(code)
        self.code = code

    


class Quantity():
    def validate(quantity):
        if type(quantity) != int:
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise Error("Quantity must be greater than 0")
        if quantity > 1000:
            raise Error("Quantity can't be greater than 1000")
        return quantity
    
    def __init__(self, quantity):
        self.quantity = self.validate(quantity)

    @property
    def quantity(self):
        return self.quantity.deepcopy()

class ShoppingCart(object):
    #Creates shopping cart objects for users of our fine website.

    def __init__(self, customer_id):
        self.cart_id = uuid.uuid4()
        self.customer_id = validate_customer_id(customer_id)
        self.items_in_cart = {}

    @property
    def cart_id(self):
        return self.cart_id.deepcopy()
    
    @property
    def customer_id(self):
        return self.customer_id.deepcopy()
    
    @property
    def items_in_cart(self):
        return self.items_in_cart.deepcopy()

    def add_item(self, product, quantity):
        # validate SKU
        # validate product is in catalog
        Quantity.validate(quantity)
        if product in self.items_in_cart:
            self.items_in_cart[product] += quantity
        else:
            self.items_in_cart[product] = quantity
        

    def remove_item(self, product, quantity):
        # Remove product from the cart.
        # validate SKU
        if product in self.items_in_cart:
            if quantity > self.items_in_cart[product]:
                print ("Quantity requested exceeds quantity in cart.")
            else:
                self.items_in_cart[product] -= quantity
                print (quantity + " of " + product + " removed.")
        else:
            print (product + " is not in the cart.")
            
