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

catalog = {
    "ABC_DEF_21": {
        "sku": "ABC_DEF_21",
        "description": "Widget",
        "price": 10.0,
    },
    "ZZZ_BOB_77": {
        "sku": "ZZZ_BOB_77",
        "description": "Thing",
        "price": 20.0,
    },
    "XXX_ROB_77": {
        "sku": "XXX_ROB_77",
        "description": "Cosa",
        "price": 15.0,
    },
    "YYY_JIL_77": {
        "sku": "YYY_JIL_77",
        "description": "Stuff",
        "price": 200.0,
    },
    "WWW_BIL_77": {
        "sku": "WWW_BIL_77",
        "description": "Cool stuff",
        "price": 0.1,
    }
}

inventory = {
  "ABC_DEF_21": 100,
  "ZZZ_BOB_77": 200,
  "XXX_ROB_77": 300,
  "YYY_JIL_77": 400,
  "WWW_BIL_77": 500
}

"""
Validates whether or not the desired quantity is available in the inventory
"""
def validate_in_inventory(sku, desired_quantity):
    if sku not in inventory:
        raise ValueError(f"Invalid SKU: {sku}")
    if desired_quantity > inventory[sku]:
        raise ValueError("Desired quantity exceeds actual inventory")

"""
Validates whether or not the catalog has the SKU
"""
def validate_in_catalog(sku):
    if sku not in catalog:
        raise ValueError(f"Invalid SKU: {sku}")

"""
Checks to see if a customer id follows the specified format
"""
def validate_customer_id(customer_id):
    valid_id = re.match(r'[a-zA-Z]{3}\d{5}[a-zA-Z]{2}[-][A|Q]', customer_id)
    if not valid_id:
        raise Exception("Not a valid customer id")
    return customer_id

"""
Checks if object is string and is under a certain length
"""
def validated_string(value, max_length):
    if not isinstance(value, str):
        raise ValueError("Value must be a string")
    if len(value) > max_length:
        raise ValueError(f"Value must be no more than {max_length} characters")
    return value


"""
Checks to see if a number is in bounds
"""
def validated_number(value, minimum, maximum):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")
    if value < minimum:
        raise ValueError(f"Value must be at least {minimum}")
    if value > maximum:
        raise ValueError(f"Value must be at most {maximum}")
    return value

"""
Class for an item that a customer can purchase
"""
class Item():
    #Creates an item object to be placed in the shopping cart.
    def __init__(self, name, price, sku, description):
        self._name = validated_string(name, 32)
        self._price = validated_number(price, .01, 999999.99)
        self._sku = SKU.validated(sku)
        self._description = validated_string(description, 1000)

    @property
    def item_id(self):
        return self._sku

    @property
    def item_name(self):
        return self._name

    @property
    def price(self):
        return self._price


"""
SKU class to validate SKUs
"""
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
        code = self.validated(code)
        self._code = code
    
    @property
    def sku(self):
        return self._code

"""
Quantity class to validate quantities of an item
"""
class Quantity():

    def validate(quantity):
        if type(quantity) != int:
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if quantity > 1000:
            raise ValueError("Quantity can't be greater than 1000")
        return quantity
    
    def __init__(self, quantity):
        self._quantity = Quantity.validate(quantity)

    @property
    def quantity(self):
        return self._quantity

"""
The Shopping Cart class
"""
class ShoppingCart:
    #Creates shopping cart objects for users of our fine website.
    def __init__(self, customer_id):
        self._cart_id = uuid.uuid4()
        self._customer_id = validate_customer_id(customer_id)
        self._items_in_cart = {}

    @property
    def cart_id(self):
        return self._cart_id
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def items_in_cart(self):
        return self._items_in_cart.deepcopy()
    
    def validate_in_cart(self, sku):
        SKU.validated(sku)
        validate_in_catalog(sku)
        if sku in self._items_in_cart:
            return True
        else:
            raise ValueError("item not in cart")

    def add_item(self, sku, quantity):
        SKU.validated(sku)
        Quantity.validate(quantity)
        validate_in_catalog(catalog, sku)
        validate_in_inventory(sku, quantity)
        self._items_in_cart[sku] = self._items_in_cart.get(sku, 0) + quantity

    def remove_item(self, sku):
        self.validate_in_cart(sku)
        self._items_in_cart.pop(sku)

    def update_item_quantity(self, sku, quantity):
        Quantity.validated(quantity)
        validate_in_inventory(sku, quantity)
        self.validate_in_cart(sku)
        self._items_in_cart[sku] = int(quantity)

    def total_cost(self):
        cost = 0
        for item in self._items_in_cart:
            cost += item.price
        return cost
