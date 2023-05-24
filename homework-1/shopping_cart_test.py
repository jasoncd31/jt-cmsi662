import unittest

from shopping_cart import ShoppingCart, SKU, Quantity, validated_string, validated_customer_id

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # customer ids must have the following form: 3 letters, 5 numbers, 2 letters, a dash, and finally an A or a Q
        self.cart = ShoppingCart("ABC12345DE-A")
        self.cart.add_item("ABC_DEF_21", 1)
        self.cart.add_item("ZZZ_BOB_77", 2)

    def test_cart_price(self):
        self.assertEqual(self.cart.total_cost(), 50.0)

    def test_cart_remove(self):
        self.cart.remove_item("ABC_DEF_21")

    # Testing SKUs
    def test_SKU_valid(self):
        self.assertEqual(SKU("ABC_DEF_21").sku, "ABC_DEF_21")

    def test_SKU_invalid(self):
        with self.assertRaises(TypeError):
            SKU("JasonRoxs")
        with self.assertRaises(TypeError):
            SKU(5)
    
    #Test quantity added is positive
    def test_add_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("ABC_DEF_21", 0)
        with self.assertRaises(ValueError):
            self.cart.add_item("ABC_DEF_21", -3)
        with self.assertRaises(ValueError):
            self.cart.update_item_quantity("ABC_DEF_21", 0)
        with self.assertRaises(ValueError):
            self.cart.update_item_quantity("ABC_DEF_21", -4)
        with self.assertRaises(ValueError):
            self.cart.add_item("YYY_JIL_77", 999)

    # test add
    def test_add(self):
        self.cart.add_item("YYY_JIL_77", 7)
        self.assertTrue("YYY_JIL_77" in self.cart.items_in_cart)
        
    # Test customer id
    def test_customer_id_valid(self):
        self.assertEqual(validated_customer_id("ABC12345DE-A"), "ABC12345DE-A")
    
    def test_customer_id_invalid(self):
        with self.assertRaises(Exception):
            validated_customer_id("JasonRoxs")
        with self.assertRaises(Exception):
            validated_customer_id("ABC12345DE-1")
        with self.assertRaises(Exception):
            validated_customer_id("ABC12345DE-")

    # test string
    def test_string_valid(self):
        self.assertEqual(validated_string("ABC_DEF_21", 32), "ABC_DEF_21")

    def test_string_invalid(self):
        with self.assertRaises(ValueError):
            validated_string(7, 32)
        with self.assertRaises(Exception):
            validated_string("HiDrToalIfYouAreReadingThisINeedToMakeAVeryLongStringToTestThisFunction", 64)
        with self.assertRaises(ValueError):
            validated_string(False, 32)
    
    def test_remove(self):
        with self.assertRaises(ValueError):
            self.cart.remove_item("XXX_ROB_77")
        with self.assertRaises(TypeError):
            self.cart.remove_item("XXXee_ROB_77")
        with self.assertRaises(ValueError):
            self.cart.remove_item("XXD_ROB_77")
        self.cart.add_item("YYY_JIL_77", 7)
        self.cart.remove_item("YYY_JIL_77")
        self.assertFalse("YYY_JIL_77" in self.cart.items_in_cart)

    def test_update(self):
        self.cart.add_item("YYY_JIL_77", 7)
        self.assertEqual(self.cart.items_in_cart["YYY_JIL_77"], 7)
        self.cart.add_item("YYY_JIL_77", 3)
        self.assertEqual(self.cart.items_in_cart["YYY_JIL_77"], 10)
        self.cart.update_item_quantity("YYY_JIL_77", 5)
        self.assertEqual(self.cart.items_in_cart["YYY_JIL_77"], 5)
        with self.assertRaises(ValueError):
            self.cart.update_item_quantity("YYY_JIL_77", 0)
        with self.assertRaises(ValueError):
            self.cart.update_item_quantity("YYY_JIL_77", -5)
        with self.assertRaises(ValueError):
            self.cart.update_item_quantity("YYY_JIL_77", 999)

    def test_properties(self):
        self.cart.items_in_cart.update({"hello": 4})
        self.assertFalse("hello" in self.cart.items_in_cart)
        customer_id = self.cart.customer_id
        customer_id = "new_id"
        self.assertFalse(customer_id == self.cart.customer_id)
        with self.assertRaises(AttributeError):
            self.cart.customer_id = "ABC12345DE-Q"


if __name__ == '__main__':
    unittest.main()


#     def test_cart_remove(self):
#         self.cart.remove_item(Item('Milk', 3.50))
#         self.assertEqual(len(self.cart), 0)

#     def test_cart_remove_error(self):
#         with self.assertRaises(ValueError):
#             self.cart.remove_item(Item('Milk', 4.50))

#     def tearDown(self):
#         del self.cart