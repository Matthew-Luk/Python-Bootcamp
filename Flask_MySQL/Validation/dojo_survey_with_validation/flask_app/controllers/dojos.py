from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods = ["POST"])
def process():
    if Dojo.validate_dojo(request.form):
        Dojo.save(request.form)
        return redirect('/results')
    return redirect("/")

@app.route('/results')
def results():
    return render_template("results.html", survey = Dojo.get_last_survey())