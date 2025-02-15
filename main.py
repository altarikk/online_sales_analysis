from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    manager = ProductManager()
    korpa = Cart()
    
    p1 = Product("Televizor", 120000, 3)
    p2 = Product("Laptop", 95000, 4)
    p3 = Product("Smartphone", 15000, 6)
    
    # Dodavanje proizvoda
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Dodavanje proizvoda u korpu
    korpa.add_product(p1)
    korpa.add_product(p2)
    korpa.add_product(p3)

    # Prikaz
    manager.display_products()
    manager.total_value()
    
    korpa.show_cart()
    print(f"Ukupno za naplatu: {korpa.total_price():.2f}.")

if __name__ == "__main__":
    main()