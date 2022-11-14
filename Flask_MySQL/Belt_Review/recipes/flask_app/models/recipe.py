from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Recipe:
    db = "recipes"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.date_cooked = data["date_cooked"]
        self.under = data["under"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.users = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes(user_id,name,description,instruction,date_cooked,under) VALUES(%(user_id)s,%(name)s,%(description)s,%(instruction)s,%(date_cooked)s,%(under)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET (user_id=%(user_id)s, name=%(name)s, description=%(description)s, instruction=%(instruction)s, date_cooked=%(date_cooked)s, under=%(under)s) WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users ON users.id = user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        recipe = cls(row)
        i = {
            "id":row["users.id"],
            "first_name":row["first_name"],
            "last_name":row["last_name"],
            "email":row["email"],
            "password":row["password"],
            "created_at":row["users.created_at"],
            "updated_at":row["users.updated_at"]
        }
        recipe.users = User(i)
        print(row)
        return recipe

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) < 2:
            flash("Name must be at least 3 characters", "create_recipe")
            is_valid = False
        if len(recipe["description"]) < 2:
            flash("Description must be at least 3 characters", "create_recipe")
            is_valid = False
        if len(recipe["instruction"]) < 2:
            flash("Instruction must be at least 3 characters", "create_recipe")
            is_valid = False
        return is_valid
    
    @classmethod
    def recipes_with_users(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = user_id;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        if len(results) < 1:
            return False
        all_recipes = []
        for row in results:
            recipe = cls(row)
            i = {
                "id":row["users.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["users.created_at"],
                "updated_at":row["users.updated_at"]
            }
            recipe.users = User(i)
            all_recipes.append(recipe)
        return all_recipes