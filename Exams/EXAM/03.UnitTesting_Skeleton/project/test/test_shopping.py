import unittest

# from shopping_cart import ShoppingCart


from project.shopping_cart import ShoppingCart


class ShoppingCartTest(unittest.TestCase):

    @staticmethod
    def _create_shopping_cart():
        name = 'MyShop'
        budget = 100
        return ShoppingCart(name, budget)

    def test_init(self):
        name = 'MyShop'
        budget = 1000
        cart = ShoppingCart(name, budget)
        self.assertEqual(name, cart.shop_name)
        self.assertEqual(budget, cart.budget)
        self.assertEqual({}, cart.products)

    def test_name_small_letter(self):
        name = 'myshop'
        budget = 1000
        msg = "Shop must contain only letters and must start with capital letter!"
        with self.assertRaises(ValueError) as context:
            ShoppingCart(name, budget)
        self.assertEqual(msg, str(context.exception))

    def test_name_not_alpha(self):
        name = '9mimi'
        budget = 1000
        msg = "Shop must contain only letters and must start with capital letter!"
        with self.assertRaises(ValueError) as context:
            ShoppingCart(name, budget)
        self.assertEqual(msg, str(context.exception))

    def test_add_to_cart_valid(self):
        product = 'meat'
        price = 99.9
        cart = self._create_shopping_cart()
        actual_msg = cart.add_to_cart(product, price)
        expected = f"{product} product was successfully added to the cart!"
        self.assertEqual(expected, actual_msg)

    def test_add_to_cart_bad_price(self):
        product = 'meat'
        price = 100.0
        cart = self._create_shopping_cart()
        expected = f"Product {product} cost too much!"
        with self.assertRaises(ValueError) as context:
            cart.add_to_cart(product, price)
        self.assertEqual(expected, str(context.exception))

    def test_remove_from_cart_valid(self):
        product = 'meat'
        price = 99.9
        cart = self._create_shopping_cart()
        cart.add_to_cart(product, price)
        expected_msg = f"Product {product} was successfully removed from the cart!"
        actual_msg = cart.remove_from_cart(product)
        self.assertEqual(expected_msg, actual_msg)
        self.assertEqual({}, cart.products)

    def test__remove_from_cart_bad_product(self):
        product = 'meat'
        price = 99.9
        cart = self._create_shopping_cart()
        cart.add_to_cart(product, price)
        bad_product = 'apple'
        expected_msg = f"No product with name {bad_product} in the cart!"
        with self.assertRaises(ValueError) as context:
            cart.remove_from_cart(bad_product)
        self.assertEqual(expected_msg, str(context.exception))

    def test__add(self):
        name1 = 'NameOne'
        name2 = 'NameTwo'
        budget1 = 1
        budget2 = 2
        cart1 = ShoppingCart(name1, budget1)
        cart2 = ShoppingCart(name2, budget2)
        product1 = 'meat'
        price1 = 1
        cart1.add_to_cart(product1, price1)
        product2 = 'apple'
        price2 = 2
        cart2.add_to_cart(product2, price2)
        new_cart = cart1 + cart2
        self.assertEqual(name1 + name2, new_cart.shop_name)
        self.assertEqual(budget1 + budget2, new_cart.budget)
        cart1.products.update(cart2.products)
        self.assertEqual(cart1.products, new_cart.products)

    def test_buy_products_valid(self):
        cart = self._create_shopping_cart()
        cart.add_to_cart('meat', 50.0)
        cart.add_to_cart('apple', 49.9)
        total_sum = 0
        for price in cart.products.values():
            total_sum += price
        expected = f'Products were successfully bought! Total cost: {total_sum:.2f}lv.'
        actual_msg = cart.buy_products()
        self.assertEqual(expected, actual_msg)

    def test_buy_products__bad_budget(self):
        cart = self._create_shopping_cart()
        cart.add_to_cart('meat', 50.0)
        cart.add_to_cart('apple', 50.1)
        total_sum = 0
        for price in cart.products.values():
            total_sum += price
        expected = f"Not enough money to buy the products! Over budget with {total_sum - cart.budget:.2f}lv!"
        with self.assertRaises(ValueError) as context:
            cart.buy_products()
        self.assertEqual(expected, str(context.exception))


if __name__ == '__main__':
    unittest.main()
