from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def flying_dutchman():
    return render_template('index.html')

pageloads = 0

@app.route('/palm', methods=['POST','GET'])
def login():
    pwd = request.form['password']
    thekey = 'fidel1o'
    if pwd == thekey:
        return render_template('main.html')
        global pageloads += 1
    else:
        return pwd
    

@app.route('/sister')
def sheistywearer():
    return 'aishwaya is my sister and she loves to commit CRIMES that are ILLEGAL because she is EVIL and a BAD person. also she is cute.'
