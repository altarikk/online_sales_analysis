class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)
    
    def total_price(self):
        total = sum(item.price for item in self.cart_items)
        return total
    
    def show_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Sadržaj korpe:")
            for item in self.cart_items:
                print(item)
