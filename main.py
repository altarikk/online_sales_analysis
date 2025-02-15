from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    manager = ProductManager()
    korpa = Cart()
    
    # Dodavanje nekoliko proizvoda
    p1 = Product("Televizor", 120000, 3)
    p2 = Product("Laptop", 95000, 4)
    p3 = Product("Smartphone", 15000, 6)
    
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Dodavanje proizvoda u korpu
    korpa.add_product(p1)
    korpa.add_product(p2)
    korpa.add_product(p3)

    # Prikaz proizvoda i ukupne vrednosti
    manager.display_products()
    manager.total_value()
    
    # Prikaz sadržaja korpe i ukupnog iznosa
    korpa.show_cart()
    print(f"Ukupno za naplatu: {korpa.total_price():.2f}.")

if __name__ == "__main__":
    main()