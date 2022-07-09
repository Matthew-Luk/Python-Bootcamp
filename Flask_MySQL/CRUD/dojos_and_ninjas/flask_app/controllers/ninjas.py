from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route("/create")
def create():
    return redirect("/ninjas")

@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninja.html",all_dojos = dojos)

@app.route("/ninjas/create", methods=["POST"])
def ninja_create():
    Ninja.save(request.form)
    return redirect("/dojos")