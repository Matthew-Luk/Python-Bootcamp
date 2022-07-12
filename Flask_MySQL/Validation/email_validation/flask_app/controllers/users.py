from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def process():
    print("Hello")
    if not User.validate_email(request.form):
        return redirect("/")
    User.save(request.form)
    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html", emails = User.get_all())

@app.route("/success/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect("/success")