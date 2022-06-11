class Store:
    def __init__(self, name, list):
        self.name = name
        self.list = list

    def add_product(self, new_product):
        self.new_product = new_product
        self.list.append(new_product)

    def sell_product(self, id):
        pass

    def inflation(self, percent_increase):
        pass

    def set_clearance(self, category, percent_discount):
        pass

    def print_store(self):
        print(f"Store name: {self.name}, Items: {self.new_product.name}")

class Product:
    products = []
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price * (1 + percent_change)
        else:
            self.price = self.price * (1 - percent_change)

    def print_info(self):
        print(f"Item: {self.name} Category: {self.category} Price: {self.price}")

storage = []

target = Store("Target", storage)
tp = Product("toilet paper", 2.99, "cleaning")
water = Product("water", 3.99, "consumable")
target.add_product(water)
target.add_product(tp)
water.print_info()
target.print_store()