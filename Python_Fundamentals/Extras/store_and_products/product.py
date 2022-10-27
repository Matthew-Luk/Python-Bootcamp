class Product:

    class_counter = 0
    def __init__(self, name, price, category):
        self.id = Product.class_counter
        self.name = name
        self.price = price
        self.category = category
        Product.class_counter += 1

    # Can either use this method or the all_products method and print(product), they will return the same thing.
    def __str__(self) -> str:
        return (f"Product name: {self.name}, Product price: ${self.price}, Product category: {self.category}")

    def print_info(self):
        print(f"Item name: {self.name}, Item price: ${self.price}, Item category: {self.category}")

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price + (self.price * percent_change)
        else:
            self.price = self.price - (self.price * percent_change)
        return self