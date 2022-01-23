from project.product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for item in self.products:
            if item.valid_name == product_name:
                return item

    def remove(self, product_name):
        for item in self.products:
            if item.valid_name == product_name:
                self.products.remove(item)
                return

    def __repr__(self):
        nl = '\n'
        return f"{nl.join([f'{product.valid_name}: {product.quantity}' for product in self.products])}"
