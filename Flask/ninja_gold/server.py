import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = "matthew1"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities_list' in session:
        print(session['activities_list'])
    return render_template('index.html', gold=session['gold'], activities=session['activities_list'])

@app.route('/process_money', methods=["post"])
def process_money():
    session['activities_list'] = []
    if request.form['building'] == "farm":
        a = (random.randint(10,20))
        print(a)
        session['activities_list'].append(f"Earned {a} golds from the farm!")
        session['gold'] = session['gold'] + a
    elif request.form['building'] == "cave":
        b = (random.randint(5,10))
        print(b)
        session['activities_list'].append(f"Earned {b} golds from the cave!")
        session['gold'] = session['gold'] + b
    elif request.form['building'] == "house":
        c = (random.randint(2,5))
        print(c)
        session['activities_list'].append(f"Earned {c} golds from the house!")
        session['gold'] = session['gold'] + c
    else:
        x = random.randint(1,2)
        y = (random.randint(0,50))
        print(x)
        print(y)
        if x == 1:
            session['gold'] = session['gold'] + y
            session['activities_list'].append(f"Entered a casino and earned {y} golds!")
        elif x == 2:
            session['gold'] = session['gold'] - y
            session['activities_list'].append(f"Entered a casino and lost {y} golds... Ouch..")
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)