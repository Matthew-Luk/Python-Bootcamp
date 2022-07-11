from flask import Flask, render_template, request, redirect, session
from users import Tourist
app = Flask(__name__)
app.secret_key = "matthew1"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    session['name'] = request.form['name']
    return redirect("/attractions")

@app.route("/attractions")
def attractions():
    tourists = Tourist.get_all()
    return render_template("attractions.html", all_tourists = tourists)

@app.route("/attractions/add", methods=["POST"])
def add():
    Tourist.save(request.form)
    return redirect("/attractions")

@app.route("/attractions/destroy")
def delete():
    Tourist.delete()
    return redirect("/attractions")

if __name__ == "__main__":
    app.run(debug=True)