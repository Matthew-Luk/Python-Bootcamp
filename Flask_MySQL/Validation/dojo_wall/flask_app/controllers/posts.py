from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.posts import Post
from flask_app import app

@app.route("/dashboard")
def dashboard():
    data = {
        "id":session["user_id"]
    }
    return render_template("dashboard.html", user=User.get_by_id(data), all_posts = Post.posts_with_user(), session_id = session["user_id"])

@app.route("/dashboard/post", methods=["POST"])
def add_post():
    if not Post.validate_post(request.form):
        return redirect("/dashboard")
    data = {
        "content":request.form["content"],
        "user_id":session["user_id"]
    }
    Post.save(data)
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    Post.delete(data)
    return redirect("/dashboard")