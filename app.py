from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def flying_dutchman():
    thekey = "fidel1o"
    return render_template('index.html')
    return redirect(url_for('ma'))
    return render_template('main.html')

@app.route('/ma')
def hd():
    return render_template('main.html')
    

@app.route('/sister')
def sheistywearer():
    return 'aishwaya is my sister and she loves to commit CRIMES that are ILLEGAL because she is EVIL and a BAD person. also she is cute.'
