from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojo.html", all_dojos = dojos)

@app.route("/add", methods=["POST"])
def add_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show(id):
    data = {
        "id":id
    }
    return render_template("show.html",dojo = Dojo.get_one_with_ninjas(data))