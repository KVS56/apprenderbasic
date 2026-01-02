from flask import Flask, render_template, request, redirect, url_for, session, flash
import numpy
from datetime import datetime
import markovify
app = Flask(__name__)
model = None

@app.route('/', methods=['POST', 'GET'])
def flying_dutchman():
    return render_template('index.html')

pageloads = 0

@app.route('/palm', methods=['POST','GET'])
def login():
    pwd = request.form['password']
    thekey = 'fidel1o'
    werrr = 'she1iist'
    if pwd == thekey:
        global pageloads
        pageloads += 1
        return render_template('main.html', views = pageloads)
    else:
        if pwd == werrr:
        return redirect(url_for("sister"))
    else:
        return 'no agartha for you'
    

@app.route('/sister')
def sheistywearer():
    return 'aishwaya is my sister and she loves to commit CRIMES that are ILLEGAL because she is EVIL and a BAD person. also she is cute.'


@app.route('/impala')
def ringdingdingding():
    tbxt = """
    The sun rises in the east.
    The sun sets in the west.
    The moon is bright tonight.
    The stars are shining.
    Sebastian Vettel, you are the world champion.
    Sebastian, DU BIST WELTMEISTER!
    """
    
    text_model = markovify.Text(tbxt)

    new_sentence = text_model.make_sentence()
    return new_sentence
    
