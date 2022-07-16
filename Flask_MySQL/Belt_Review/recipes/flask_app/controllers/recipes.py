from flask import redirect, render_template, request, session
from flask_app.models.recipe import Recipe
from flask_app import app
from flask_app.models.user import User

@app.route("/dashboard/create_recipe")
def create_recipe():
    return render_template("/create_recipe.html")

@app.route("/dashboard/create_recipe/add", methods = ["POST"])
def submit_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect("/dashboard/create_recipe")
    data = {
        "user_id":session["user_id"],
        "name":request.form["name"],
        "description":request.form["description"],
        "instruction":request.form["instruction"],
        "date_cooked":request.form["date_cooked"],
        "under":request.form["under"],
    }
    Recipe.save(data)
    return redirect("/dashboard")

@app.route("/dashboard/view/<int:id>")
def view_recipe(id):
    data = {
        "id":session["user_id"]
    }
    data2 = {
        "id":id
    }
    return render_template("view.html", user=User.get_by_id(data), recipe=Recipe.get_by_id(data2), recipes=Recipe.recipes_with_users())

@app.route("/dashboard/edit/<int:id>")
def edit_recipe(id):
    data = {
        "id":id
    }
    Recipe.update(data)
    return render_template("edit.html", recipe=Recipe.get_by_id(data))