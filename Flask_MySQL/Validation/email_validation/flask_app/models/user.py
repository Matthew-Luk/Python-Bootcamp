from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "email"
    def __init__(self,data):
        self.id = data["id"]
        self.email_address = data["email_address"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        user = []
        for row in results:
            user.append(cls(row))
        return user
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails(email_address) VALUES(%(email_address)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_email(email):
        print("Hello")
        is_valid = True
        query = "SELECT * FROM emails WHERE email_address = %(email_address)s;"
        results = connectToMySQL(User.db).query_db(query,email)
        if len(results) > 0:
            flash("Email has already been entered.")
            is_valid = False
        if not EMAIL_REGEX.match(email["email_address"]):
            flash("Invalid Email Address")
            is_valid = False
        return is_valid
