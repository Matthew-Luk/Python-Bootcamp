from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route("/users/new")
def new_user():
    return render_template("create.html")

@app.route('/users/create', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)