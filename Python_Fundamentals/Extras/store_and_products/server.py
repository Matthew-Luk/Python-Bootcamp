from store import Store
from product import Product

target = Store("Target")
product1 = Product("Play Station 5", 500, "Electronics")
product2 = Product("Squishmallow", 25, "Toys")
product3 = Product("CDG Hoodies", 300, "Clothing")
target.add_product(product1)
target.add_product(product2)
target.add_product(product3)
target.sell_product(0)
target.inflation(0.05)
target.set_clearance("Clothing", 0.5)
target.all_products()