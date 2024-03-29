from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "email_validation"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        user = []
        for row in results:
            user.append(cls(row))
        return user
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(first_name,last_name,email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(f'Here are the results:{results}')
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) > 0:
            flash("Email has already been entered.")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid Email Address")
            is_valid = False
        if len(user["first_name"]) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user["last_name"]) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        return is_valid