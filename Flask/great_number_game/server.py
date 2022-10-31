import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = "matthew1"

@app.route('/')
def index():
    if "number" not in session:
        session['number'] = random.randint(1,100)
    print(session['number'])
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template("index.html", correct_number=session['number'], attempts=session['attempts'])

@app.route('/guess', methods=['POST'])
def guess():
    try:
        session['guess'] = int(request.form['guess'])
        session['attempts'] = session['attempts'] + 1
        return redirect('/')
    except ValueError:
        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   