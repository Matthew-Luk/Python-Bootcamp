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
    return render_template("readall.html", all_users = users)

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
    user_id = User.save(data)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("readone.html", user=User.get_one(data))

@app.route('/users/<int:id>/destroy')
def delete(id):
    data ={
        "id":id
    }
    User.delete(data)
    return redirect("/users")

@app.route('/users/<int:id>/edit')
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit.html", user=User.get_one(data))

@app.route('/users/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)