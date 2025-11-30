from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def flying_dutchman():
    return render_template('index.html')
    
@app.route('/', methods=['POST', 'GET'])
def login():
    pwd = request.form['password']
    key = 'fidel1o'
    if pwd == key:
        return render_template('main.html')
    else:
        return 'doubtfire? gambit declined', pwd, 'is not correct'
    

@app.route('/sister')
def sheistywearer():
    return 'aishwaya is my sister and she loves to commit CRIMES that are ILLEGAL because she is EVIL and a BAD person. also she is cute.'
