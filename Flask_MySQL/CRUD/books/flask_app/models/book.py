from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db = "books"
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.db).query_db(query)
        all_books = []
        for row in results:
            all_books.append(cls(row))
        return all_books

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books(title,num_of_pages) VALUES(%(title)s,%(num_of_pages)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM books WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        book = cls(row)
        return book

    @classmethod
    def authors_who_favorited():
        pass