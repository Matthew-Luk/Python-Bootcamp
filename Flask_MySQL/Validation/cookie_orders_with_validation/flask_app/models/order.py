from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    db = "cookie_orders"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.number_of_boxes = data["number_of_boxes"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders"
        results = connectToMySQL(cls.db).query_db(query)
        all_orders = []
        for row in results:
            all_orders.append(cls(row))
        return all_orders

    @classmethod
    def save(cls,data):
        query = "INSERT INTO orders(name,cookie_type,number_of_boxes) VALUES(%(name)s,%(cookie_type)s,%(number_of_boxes)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE orders SET name=%(name)s, cookie_type=%(cookie_type)s, number_of_boxes=%(number_of_boxes)s WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM orders WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) > 1:
            return False
        row = results[0]
        order = cls(row)
        return order

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM orders WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order["name"]) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(order["cookie_type"]) < 2:
            flash("Cookie type must be at least 2 characters.")
            is_valid = False
        if int(order["number_of_boxes"]) < 1:
            flash("Please enter a valid number of boxes")
            is_valid = False
        return is_valid