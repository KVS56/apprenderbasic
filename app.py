from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def flying_dutchman():
    thekey = "fidel1o"
    return render_template('index.html')
    return redirect(url_for('ma'))
    return render_template('main.html')

@app.route('/log', methods=['POST', 'GET'])
def login():
    pwd = request.form['password']
    ken = 7
    if pwd == thekey:
        return render_template('main.html')
    else:
        return 'doubtfire? gambit declined'
    

@app.route('/sister')
def sheistywearer():
    return 'aishwaya is my sister and she loves to commit CRIMES that are ILLEGAL because she is EVIL and a BAD person. also she is cute.'
