from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db = "books"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.fav_books = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors(name) VALUES(%(name)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(cls.db).query_db(query)
        all_authors = []
        for row in results:
            all_authors.append(cls(row))
        return all_authors

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return results