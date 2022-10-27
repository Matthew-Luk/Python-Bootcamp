class Store:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def all_products(self):
        for product in self.products:
            print (f"Product name: {product.name}, Product price: ${product.price}, Product category: {product.category}")

    def sell_product(self,id):
        for product in self.products:
            if product.id == id:
                removed_element = self.products.pop(id)
                print(f"Removed item: {removed_element}")

    def inflation(self, percent_increase):
        for product in self.products:
            product.price = product.price + (product.price * percent_increase)

    def set_clearance(self,category,percent_discount):
        for product in self.products:
            if product.category == category:
                product.price = product.price - (product.price * percent_discount)