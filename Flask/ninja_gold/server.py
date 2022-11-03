import random
import datetime
import time
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = "matthew1"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities_list' not in session:
        session['activities_list'] = []
    if 'attempts' not in session:
        session['attempts'] = 0
    print(session['attempts'])
    return render_template('index.html', gold=session['gold'], activities=session['activities_list'], attempts=session['attempts'])

@app.route('/process_money', methods=["post"])
def process_money():
    x = time.localtime()
    date = time.strftime("%Y/%m/%d, %I:%M:%p", x)
    if request.form['building'] == "farm":
        a = (random.randint(10,20))
        session['activities_list'].append(f"Earned {a} golds from the farm! ({date})")
        session['gold'] = session['gold'] + a
    elif request.form['building'] == "cave":
        b = (random.randint(5,10))
        session['activities_list'].append(f"Earned {b} golds from the cave! ({date})")
        session['gold'] = session['gold'] + b
    elif request.form['building'] == "house":
        c = (random.randint(2,5))
        session['activities_list'].append(f"Earned {c} golds from the house! ({date})")
        session['gold'] = session['gold'] + c
    elif request.form['building'] == "casino":
        x = random.randint(1,2)
        y = (random.randint(0,50))
        if x == 1:
            session['gold'] = session['gold'] + y
            session['activities_list'].append(f"Entered a casino and earned {y} golds! ({date})")
        elif x == 2:
            session['gold'] = session['gold'] - y
            session['activities_list'].append(f"Entered a casino and lost {y} golds... Ouch.. ({date})")
    session['attempts'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)