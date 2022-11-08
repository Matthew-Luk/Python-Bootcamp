from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app

@app.route("/add_book")
def add_book():
    return render_template("books.html", all_books = Book.get_all())

@app.route("/add_book_submit", methods = ["POST"])
def add_book_submit():
    Book.save(request.form)
    return redirect("/add_book")

@app.route("/book_show/<int:id>")
def book_show(id):
    data = {
        "id":id,
        "book_id":id
    }
    return render_template("book_show.html", book = Book.get_by_id(data), all_authors = Author.get_all())