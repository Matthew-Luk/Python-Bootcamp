from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def route1():
    return render_template("index.html", row=8, col=8, color1="red", color2="black")

@app.route('/<int:num>')
def route2(num):
    return render_template("index.html", row=num, col=8, color1="red", color2="black")

@app.route('/<int:x>/<int:y>')
def route3(x,y):
    return render_template("index.html", row=x, col=y, color1="red", color2="black")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def route4(x,y,color1,color2):
    return render_template("index.html", row=x, col=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)