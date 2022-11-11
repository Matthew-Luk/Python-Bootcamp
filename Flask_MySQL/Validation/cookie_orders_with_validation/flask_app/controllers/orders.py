from flask import render_template, redirect, request, session
from flask_app.models.order import Order
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html", all_orders = Order.get_all())

@app.route("/cookies/new")
def new_order():
    return render_template("order.html")

@app.route("/cookies/new/submit", methods=["POST"])
def new_order_submit():
    if not Order.validate_order(request.form):
        return redirect("/cookies/new")
    Order.save(request.form)
    return redirect("/")

@app.route("/cookies/<int:id>")
def edit_order(id):
    data = {
        "id":id
    }
    return render_template("edit.html", order = Order.get_by_id(data))

@app.route("/cookies/edit/<int:id>", methods=["POST"])
def edit_order_submit(id):
    data = {
        "id":id,
        "name":request.form["name"],
        "cookie_type":request.form["cookie_type"],
        "number_of_boxes":request.form["number_of_boxes"]
    }
    if not Order.validate_order(data):
        return redirect(f"/cookies/{data['id']}")
    Order.update(data)
    return redirect("/")

@app.route("/delete_order/<int:id>")
def delete_order(id):
    data = {
        "id":id
    }
    Order.delete(data)
    return redirect("/")