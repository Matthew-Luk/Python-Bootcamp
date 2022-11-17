from flask import redirect, render_template, request, session
from flask_app.models.rideshare import Rideshare
from flask_app import app
from flask_app.models.user import User

@app.route("/request_rideshare")
def request_rideshare():
    return render_template("request.html")

@app.route("/request_rideshare/submit", methods=["POST"])
def request_rideshare_submit():
    Rideshare.save(request.form)
    return redirect("/dashboard")