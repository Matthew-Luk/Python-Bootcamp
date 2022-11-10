from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app import app

@app.route("/")
def index():
    if 'first_name' not in session:
        session['first_name'] = ""
    if 'last_name' not in session:
        session['last_name'] = ""
    if 'email' not in session:
        session['email'] = ""
    return render_template("index.html", first_name = session['first_name'], last_name = session['last_name'], email = session['email'])

@app.route("/process",methods=["POST"])
def process():
    if not User.validate_user(request.form):
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form["last_name"]
        session["email"] = request.form["email"]
        return redirect("/")
    User.save(request.form)
    return redirect("/success")

@app.route("/success")
def success():
    session.clear()
    return render_template("success.html", all_users = User.get_all())

@app.route("/success/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect("/success")