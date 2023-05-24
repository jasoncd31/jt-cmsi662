import unittest

from shopping_cart import ShoppingCart, Item

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # customer ids must have the following form: 3 letters, 5 numbers, 2 letters, a dash, and finally an A or a Q
        self.cart = ShoppingCart("ABC12345DE-A")
        self.cart.add_item(Item('Milk', 3.50, "ABC_DEF_21", "WHITE LIQUID"))

#     def test_cart_length(self):
#         self.cart.add_item(Item('Milk', 3.50))
#         self.assertEqual(len(self.cart), 2)

#     def test_cart_price(self):
#         self.cart.add_item(Item('Milk', 3.50))
#         self.assertEqual(self.cart.price, 7)

#     def test_cart_remove(self):
#         self.cart.remove_item(Item('Milk', 3.50))
#         self.assertEqual(len(self.cart), 0)

#     def test_cart_remove_error(self):
#         with self.assertRaises(ValueError):
#             self.cart.remove_item(Item('Milk', 4.50))

#     def tearDown(self):
#         del self.cart