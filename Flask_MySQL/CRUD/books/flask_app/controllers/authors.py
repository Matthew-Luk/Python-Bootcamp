from flask import render_template, redirect, session, request
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app import app

@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def authors():
    return render_template("authors.html", all_authors = Author.get_all())

@app.route("/create_author", methods = ["POST"])
def create_author():
    Author.save(request.form)
    return redirect("/authors")

@app.route("/author_show/<int:id>")
def author_show(id):
    data = {
        "id":id,
        "author_id":id
    }
    return render_template("author_show.html", author = Author.get_by_id(data), all_books = Book.get_all())

@app.route("/add_favorite_book", methods=["POST"])
def add_favorite_book():
    data = {
        "id":request.form["author_id"]
    }
    Author.add_to_favorites(request.form)
    return redirect(f'/author_show/{data["id"]}')