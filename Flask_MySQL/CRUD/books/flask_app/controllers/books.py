from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app

@app.route("/add_book")
def add_book():
    pass