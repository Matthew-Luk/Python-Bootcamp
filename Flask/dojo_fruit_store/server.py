from flask import Flask, render_template, request, redirect
from datetime import date
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    today = date.today()
    d1 = today.strftime("%B %d, %Y")
    total = (int(request.form["strawberry"]) + int(request.form["raspberry"]) + int(request.form["apple"]) + int(request.form["blackberry"]))
    return render_template("checkout.html", d1=d1, total=total)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)