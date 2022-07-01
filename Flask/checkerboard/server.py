from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default():
    return render_template("index.html")

@app.route('/<int:num>')
def route(num):
    return render_template("index.html", num=num)

@app.route('/<int:x>/<int:y>')
def two(x,y):
    return render_template("index.html", row=x, col=y)

if __name__=="__main__":
    app.run(debug=True)