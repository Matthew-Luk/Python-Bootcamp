from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "matthew1"

@app.route('/')
def hello_world():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] = session["count"] + 1
    return render_template("index.html")

@app.route('/add')
def add():
    session["count"] = session["count"] + 1
    return redirect('/')

@app.route('/add_increment', methods=["POST"])
def add_increment():
    try:
        session["count"] = session["count"] + (int(request.form["number"])-1)
        return redirect('/')
    except ValueError:
        session["count"] = session["count"] - 1
        return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)