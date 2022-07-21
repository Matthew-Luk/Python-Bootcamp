from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Post:
    db = "dojo_wall"
    def __init__(self,data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts"
        results = connectToMySQL(cls.db).query_db(query)
        posts = []
        for row in results:
            posts.append(cls(row))
        return posts

    @classmethod
    def save(cls,data):
        query = "INSERT INTO posts(content,user_id) VALUES(%(content)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM posts WHERE posts.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def posts_with_user(cls):
        query = "SELECT * FROM users JOIN posts ON users.id = user_id ORDER BY posts.created_at DESC;"
        results = connectToMySQL(cls.db).query_db(query)
        all_posts = []
        for row in results:
            print(row)
            all_posts.append((User(row),cls(row)))
        return all_posts

    @staticmethod
    def validate_post(message):
        is_valid = True
        if len(message["content"]) < 1:
            flash("* Post must not be blank.")
            is_valid = False
        return is_valid