from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod '{product.name}' dodan u listu.")

    def display_products(self):
        if not self.products:
            print("Nema dostupnih proizvoda.")
        else:
            for product in self.products:
                product.display_info()

    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Ukupna vrijednost svih proizvoda: {total:.2f}.")

def remove_product_by_name(self, name):
        initial_count = len(self.products)
        self.products = [product for product in self.products if product.name != name]