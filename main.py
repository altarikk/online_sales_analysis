from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()
    
    # Dodavanje nekoliko proizvoda
    p1 = Product("Televizor", 120000, 3)
    p2 = Product("Laptop", 95000, 4)
    p3 = Product("Smartphone", 15000, 6)
    
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    
    # Prikaz proizvoda i ukupne vrednosti
    manager.display_products()
    manager.total_value()

if __name__ == "__main__":
    main()
